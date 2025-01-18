from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

def get_or_create(session: Session, model, defaults=None, **kwargs):
    """
    Get an instance of `model` matching the `kwargs`. 
    If it doesn't exist, create it with `defaults`.

    Args:
        session (Session): SQLAlchemy session.
        model (Base): SQLAlchemy model class.
        defaults (dict, optional): Extra fields to set when creating an instance.
        kwargs: Fields to filter the instance.

    Returns:
        tuple: (instance, created) where `created` is a boolean indicating 
               whether the instance was created.
    """
    defaults = defaults or {}
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False

    # Combine defaults with kwargs for new instance creation
    params = {**kwargs, **defaults}
    instance = model(**params)
    session.add(instance)
    try:
        session.commit()
        return instance, True
    except IntegrityError:
        session.rollback()
        # Retry fetching the instance in case it was created during a race condition
        return session.query(model).filter_by(**kwargs).first(), False
