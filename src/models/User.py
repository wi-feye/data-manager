from werkzeug.security import generate_password_hash, check_password_hash

from src import db

# default library salt length is 8
# adjusting it to 16 allow us to improve the strongness of the password
_SALT_LENGTH = 16


class User(db.Model):
    """Representation of User model."""

    # The name of the table that we explicitly set
    __tablename__ = 'User'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'email', 'firstname', 'lastname', 'password']

    # All fields of user
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(128), unique=True, nullable=False)
    firstname = db.Column(db.Unicode(128), nullable=False)
    lastname = db.Column(db.Unicode(128), nullable=False)
    password = db.Column(db.Unicode(128), nullable=False)
    authenticated = db.Column(db.Boolean, default=True)

    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)
        self.authenticated = False

    def set_password(self, password):
        '''
        According to https://werkzeug.palletsprojects.com/en/2.0.x/utils/#werkzeug.security.generate_password_hash
        generate_password_hash returns a string in the format below
        pbkdf2:sha256:num_of_iterations$salt$hash
        '''
        self.password = generate_password_hash(password, salt_length = _SALT_LENGTH)

    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])