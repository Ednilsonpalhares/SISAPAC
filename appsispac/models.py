from django.db import models

class Funcionario(models.Model):
    nome = models.CharField("Nome", max_length=200)
    matricula = models.IntegerField("Matricula")
    senha = models.CharField("Senha", max_length=16)

    def __str__(self):
        return self.nome

class Horarios(models.Model):
    HORARIOS = (
        ('Vazio', 'Indefinido'),
        ('07:00 - 08:30', '07:00 - 08:30'),
        ('08:50 - 10:20', '08:50 - 10:20'),
        ('10:30 - 12:00', '10:30 - 12:00'),
        ('13:00 - 14:30', '13:00 - 14:30'),
        ('14:50 - 16:20', '14:50 - 16:20'),
        ('16:30 - 18:00', '16:30 - 18:00'),
        ('18:00 - 19:50', '18:00 - 19:50'),
        ('20:00 - 22:00', '20:00 - 22:00'),
    )
    horarios = models.CharField(
        max_length=30,
        choices=HORARIOS,
        default='Vazio',
    )
    def __str__(self):
        return self.horarios

class Professor(Funcionario):
    def __str__(self):
        return self.nome

class Horario_Professor(models.Model):
    WEEKDAYS = (
        ('ND', 'Não definido'),
        ('SEG', 'Segunda-Feira'),
        ('TER', 'Terça-Feira'),
        ('QUA', 'Quarta-Feira'),
        ('QUI', 'Quinta-Feira'),
        ('SEX', 'Sexta-Feira'),
    )
    weekdays = models.CharField(
        max_length=25,
        choices=WEEKDAYS,
        default='ND',
    )
    horario = models.ForeignKey(Horarios)
    turma = models.CharField("Turma", max_length=150)
    disciplina = models.CharField("Disciplina", max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return self.horario.horarios + " - " + self.turma

class Sala(models.Model):
    sigla = models.CharField("Sigla", max_length=10)
    descricao = models.CharField("Descrição", max_length=100)
    def __str__(self):
        return self.sigla

class Registro_Frequencia(models.Model):
    data = models.DateField("Data do registro")
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    horario = models.ForeignKey(Horarios)
    def __str__(self):
        return self.professor.nome

class Reserva_Sala(models.Model):
    data = models.DateField("Data do Registro")
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horario = models.ForeignKey(Horarios)
    def __str__(self):
        return self.funcionario.nome