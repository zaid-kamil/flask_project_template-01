'''
Database helper functions
'''

from database import opendb

def db_save(obj):
    """Save object to database"""
    session = opendb()
    session.add(obj)
    session.commit()
    session.close()

def db_delete(obj):
    """Delete object from database"""
    session = opendb()
    session.delete(obj)
    session.commit()
    session.close()

def db_update(obj):
    """Update object in database"""
    session = opendb()
    session.merge(obj)
    session.commit()
    session.close()

def db_get(cls, id):
    """Get object from database"""
    session = opendb()
    obj = session.query(cls).get(id)
    session.close()
    return obj

def db_get_all(cls):
    """Get all objects from database"""
    session = opendb()
    objs = session.query(cls).all()
    session.close()
    return objs

def db_get_by_field(cls, **kwargs):
    """Get object from database by field"""
    session = opendb()
    obj = session.query(cls).filter_by(**kwargs).first()
    session.close()
    return obj

def db_get_by_id(cls, id):
    """Get object from database by id"""
    session = opendb()
    obj = session.query(cls).get(id)
    session.close()
    return obj

