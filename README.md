# :snake: Python Backend with Flask and SQLAlchemy

> Backend implementado em Python para a disciplina de _Desenvolvimento de Sistemas em Python_ do IFC Campus Blumenau.

## :octocat: Diagrama de classes
As classes modeladas foram: **Pessoa**(nome, cpf, email), **Disciplina**(nome, carga horária, ementa) e **EstudanteDaDisciplina**(semestre, pessoa, disciplina, mediaFinal, frequencia).

O nome da entidade EstudanteDaDisciplina foi modificado para _Student_, e ela possui relacionamentos Many-To-One tanto com a entidade Pessoa (_Person_), quanto com a entidade Disciplina (_Subject_). Ambos são relacionamentos de composição em que um _Student_ não existe sem uma pessoa ou disciplina. Dessa forma, os campos **person** e **subject** da entidade *Student* são obrigatórios; i.e., não podem ser nulos.

![diagrama-classes-ped](https://user-images.githubusercontent.com/50798315/147425974-51eeab06-8b44-42a0-8023-b2edf22572d9.png)

## :computer: Como testar?

### Instalar as dependências
```python -m pip install -r requirements.txt```

### Iniciar o servidor
Rodar o arquivo _servidor.py_ utilizando a sua IDE de preferência, ou através do comando:

```python server.py```

Após isso, o backend irá rodar na porta 5000.

## :motorway: Rotas Disponíveis

### :standing_person: Persons (Pessoas)

#### [GET] /persons
> Para ver a lista de pessoas cadastradas
> 
> Aceita filtro pelo campo 'name'. Exemplo:
> ```[POST] http://localhost:5000/persons?name=jo```
> irá realizar uma busca por pessoas que possuam 'jo' em seus nomes, ignorando se o texto é maiúsculo ou minúsculo


#### [GET] /persons/<person_id>
> Para ver os dados da pessoa de id igual a _person_id_

#### [POST] /persons
> Para incluir uma nova pessoa
> ```
> {
>     "name": "Giovana da Silva",
>     "cpf": "02938128391"
> }
> ```

#### [DELETE] /persons/<person_id>
> Para excluir o registro da pessoa de id igual a _person_id_


### :books: Subjects (Disciplinas)

#### [GET] /subjects
> Para ver a lista de disciplinas cadastradas
> 
> Aceita filtro pelo campo 'name'. Exemplo:
> ```[POST] http://localhost:5000/subjects?name=ma```
> irá realizar uma busca por pessoas que possuam 'ma' em seus nomes, ignorando se o texto é maiúsculo ou minúsculo


#### [GET] /subjects/<subject_id>
> Para ver os dados da disciplina de id igual a _subject_id_

#### [POST] /subjects
> Para incluir uma nova disciplina
> ```
> {
>     "name": "Biologia",
>     "workload": 60,
>     "syllabus": "Ementa da disciplina de Biologia"
> }
> ```

#### [DELETE] /subjects/<subject_id>
> Para excluir o registro da disciplina de id igual a _subject_id_


### :student: Students (Estudantes das Disciplinas)

#### [GET] /students
> Para ver a lista de estudantes relacionados às disciplinas

#### [GET] /students/<student_id>
> Para ver os dados do estudante de id igual a _student_id_

#### [POST] /students
> Para incluir um novo estudante
> ```
> {
>     "semester": 4,
>     "final_score": 9.5,
>     "frequency": 88.7,
>     "person_id": 2,
>     "subject_id": 3
> }
> ```

#### [DELETE] /students/<student_id>
> Para excluir o registro do estudante de id igual a _student_id_
