import pytest
import uuid
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:Akkerman@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'test_students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)


@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()


def test_add_student(db_session):
    """Тест на добавление сущности"""
    unique_name = f"Ivan_{uuid.uuid4().hex[:6]}"
    new_student = Student(name=unique_name, age=20)

    db_session.add(new_student)
    db_session.commit()

    assert new_student.id is not None
    student_from_db = db_session.query(Student).filter_by(
        name=unique_name
        ).first()
    assert student_from_db is not None
    assert student_from_db.age == 20

    db_session.delete(student_from_db)
    db_session.commit()


def test_update_student(db_session):
    """Тест на изменение сущности"""
    unique_name = f"Peter_{uuid.uuid4().hex[:6]}"
    student = Student(name=unique_name, age=25)
    db_session.add(student)
    db_session.commit()

    student.name = f"{unique_name}_Updated"
    student.age = 26
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(
        id=student.id
        ).first()
    assert updated_student.name == f"{unique_name}_Updated"
    assert updated_student.age == 26

    db_session.delete(updated_student)
    db_session.commit()


def test_delete_student(db_session):
    """Тест на удаление сущности"""
    unique_name = f"Anna_{uuid.uuid4().hex[:6]}"
    student = Student(name=unique_name, age=22)
    db_session.add(student)
    db_session.commit()
    student_id = student.id

    student_to_delete = db_session.query(Student).filter_by(
        id=student_id
        ).first()
    db_session.delete(student_to_delete)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(
        id=student_id
        ).first()
    assert deleted_student is None
