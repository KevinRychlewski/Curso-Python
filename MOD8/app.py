# PERMITIRA CRIAR UMA API
from flask import Flask
# PERMITIRA CRIAR UM BANCO DE DADOS
from flask_sqlalchemy import SQLAlchemy

# Criar uma API flask
app = Flask(__name__)
# criar uma instancia de sqlalchemy
app.config['SECRET_KEY'] = 'FSDGW23WRFASDZAF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
db:SQLAlchemy
# definir a estrutura da tabela postagem
# toda postagem deve ter: id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer,db.ForeignKey('autor.id_autor'))
    
# definir a estrutura da tabela autor
# toda tabela de autor deve ter: id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')
# Executar o comando para criar o banco de dados
with app.app_context():
    db.drop_all()
    db.create_all()
    # criar usuarios administradores
    autor = Autor(nome='kevin',email='kevin@gmail.com',senha='12345',admin=True)
    db.session.add(autor)
    db.session.commit()