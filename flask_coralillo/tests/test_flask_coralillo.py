import flask
from flask_coralillo import Coralillo
import unittest


class InitTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask.Flask(__name__)

    def test_constructor(self):
        """Test that a constructor with app instance will initialize the
        connection"""
        coralillo = Coralillo(self.app)

        assert hasattr(coralillo, 'lua')
        assert hasattr(coralillo, 'redis')


    def test_init_app(self):
        """Test that a constructor without app instance will not initialize the
        connection.

        After Coralillo.init_app(app) is called, the connection will be
        initialized."""
        coralillo = Coralillo()

        assert coralillo._engine is None

        coralillo.init_app(self.app)

        assert coralillo._engine is not None
        assert coralillo.redis is not None
        assert coralillo.lua is not None

    def test_custom_prefix(self):
        """Test that config prefixes enable distinct connections"""
        self.app.config['DBA_URL'] = 'redis://localhost:6379/1'
        self.app.config['DBB_URL'] = 'redis://localhost:6379/2'

        coralillo_a = Coralillo(self.app, config_prefix='DBA')
        coralillo_b = Coralillo(self.app, config_prefix='DBB')

        assert coralillo_a.redis.connection_pool.connection_kwargs['db'] == 1
        assert coralillo_b.redis.connection_pool.connection_kwargs['db'] == 2

    def test_custom_id_function(self):
        def simple_ids():
            from random import choice

            return ''.join(choice('1234567890') for c in range(10))

        eng = Coralillo(self.app)
        custom_eng = Coralillo(self.app, id_function=simple_ids)

        old_id = eng.id_function()
        new_id = custom_eng.id_function()

        self.assertEqual(len(old_id), 32)
        self.assertEqual(len(new_id), 10)


if __name__ == '__main__':
    unittest.main()
