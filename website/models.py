from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, nullable=False)
    role = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    birth = Column(DateTime)
    forum = relationship('ATOModel', primaryjoin='(UserModel.id==ATOModel.owner)', backref='user')
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}: EMPID{self.employee_id}'

    def __repr__(self):
        return (
            f'UserModel(id={self.id}, first_name={self.first_name}, last_name={self.last_name},'
            f'employee_id={self.employee_id}, email={self.email}, birth={self.birth},'
            f'created={self.created})'
        )


class ATOModel(Base):
    __tablename__ = 'ato-form'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    owner = Column(Integer, ForeignKey('user.id'))
    created = Column(DateTime, default=datetime.utcnow)


# Creating seed data
users = [
    UserModel(employee_id=234567, role='security-analyst', first_name='Bob', last_name='Preston', email='bobpreston@email.com', password="secret123",  birth=datetime(1980, 5, 2)),
    UserModel(employee_id=789012, role='security-analyst', first_name='Susan', last_name='Sage', email='susansage@email.com', password="secret456", birth=datetime(1979, 1, 12)),
    UserModel(employee_id=345678, role='security-analyst', first_name='James', last_name='Button', email='jamebutton@email.com', password="secret789", birth=datetime(1981, 4, 23)),
    UserModel(employee_id=901234, role='security-analyst', first_name='Emilly', last_name='Carlton', email='emillycarlton@email.com', password="secret012",  birth=datetime(1989, 5, 2)),
    UserModel(employee_id=567890, role='security-analyst', first_name='Dave', last_name='Chapelle', email='davechapelle@email.com', password="secret345", birth=datetime(1978, 1, 12)),
    UserModel(employee_id=987654, role='security-analyst', first_name='Son', last_name='Goku', email='songoku@email.com', password="secret678", birth=datetime(1987, 4, 23)),
    UserModel(employee_id=654987, role='supervisor', first_name='Yuji', last_name='Itadori', email='yujiitadori@email.com', password="supersecret123",  birth=datetime(1986, 5, 2)),
    UserModel(employee_id=321987, role='it-director', first_name='Sasuke', last_name='Uchiha', email='sasukeuchiha@email.com', password="supersecret456", birth=datetime(1974, 1, 12)),
    UserModel(employee_id=987321, role='cisso', first_name='John', last_name='Wick', email='johnwick@email.com', password="supersecret789", birth=datetime(1971, 4, 23))
]

ato_form = [
    ATOModel(type='Hardware', status='Approved', owner=3),
    ATOModel(type='Software', status='Pending', owner=3),
    ATOModel(type='Hardware', status='Pending', owner=4),
    ATOModel(type='Hardware', status='Approved', owner=5),
    ATOModel(type='Software', status='Approved', owner=3),
    ATOModel(type='Software', status='Pending', owner=6),
    ATOModel(type='Hardware', status='Approved', owner=6),
    ATOModel(type='Hardware', status='Denied', owner=1),
    ATOModel(type='Software', status='Approved', owner=1),
    ATOModel(type='Software', status='Denied', owner=2)
]

session_maker = sessionmaker(bind=create_engine(f'postgresql://{username}:{passwd}@localhost:5432/{db_name}'))

# Create the users from seed data
def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

def create_ato_forums():
    with session_maker() as session:
        for forum in ato_form:
            session.add(forum)
        session.commit()

