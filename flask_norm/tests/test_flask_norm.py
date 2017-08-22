import flask
from flask_norm import Norm
import unittest

__all__ = ('FlaskNorm', )
__version__ = '0.1.0'


class InitTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask.Flask(__name__)

    def test_constructor(self):
        """Test that a constructor with app instance will initialize the
        connection"""
        norm = Norm(self.app)

        assert hasattr(norm, 'lua')
        assert hasattr(norm, 'redis')


    def test_init_app(self):
        """Test that a constructor without app instance will not initialize the
        connection.

        After Norm.init_app(app) is called, the connection will be
        initialized."""
        norm = Norm()
        assert norm.redis is None
        assert norm.lua is None

        norm.init_app(self.app)

        assert norm.redis is not None
        assert norm.lua is not None


    def test_custom_prefix(self):
        """Test that config prefixes enable distinct connections"""
        self.app.config['DBA_URL'] = 'redis://localhost:6379/1'
        self.app.config['DBB_URL'] = 'redis://localhost:6379/2'

        norm_a = Norm(self.app, config_prefix='DBA')
        norm_b = Norm(self.app, config_prefix='DBB')

        assert norm_a.redis.connection_pool.connection_kwargs['db'] == 1
        assert norm_b.redis.connection_pool.connection_kwargs['db'] == 2


if __name__ == '__main__':
    unittest.main()
