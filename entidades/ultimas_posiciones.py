
class UltimasPosiciones(db.Model):
    matricula = db.Column(db.String(64), primary_key=True)
    fecha_ultima_posicion = db.Column(db.String(20), nullable=False)
