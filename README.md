# :snake: Python Backend with Flask and SQLAlchemy

> Backend implementado em Python para a disciplina de _Desenvolvimento de Sistemas em Python_ do IFC Campus Blumenau.
> Implementação de 10 classes relacionadas

## :octocat: Diagrama de classes
![diagrama-uml](https://user-images.githubusercontent.com/50798315/150057313-808491ea-3dbd-424f-8d7b-8d63c7ddc8e4.png)

## :computer: Como testar?

### Instalar as dependências
```python -m pip install -r requirements.txt```

### Iniciar o servidor
Rodar o arquivo _servidor.py_ utilizando a sua IDE de preferência, ou através do comando:

```python server.py```

Após isso, o backend irá rodar na porta 5000.

## :motorway: Rotas Disponíveis

### :standing_person: Users (Pessoas)

#### [GET] /users
> Para ver a lista de usuários cadastrados
> 
> Aceita filtro pelo campo 'name'. Exemplo:
> ```[POST] http://localhost:5000/users?name=jo```
> irá realizar uma busca por pessoas que possuam 'jo' em seus nomes, ignorando se o texto é maiúsculo ou minúsculo


#### [GET] /users/<user_id>
> Para ver os dados do usuário de id igual a _user_id_

#### [POST] /users
> Para incluir um novo usuário
> ```
> {
>     "name": "João Silva",
>     "email": "joaosilva@gmail.com",
>     "password": "123456",
>     "roleId": 1
> }
> ```

#### [DELETE] /users/<user_id>
> Para excluir o registro do usuário de id igual a _user_id_


### :books: Roles (Cargos/Autoridades)
> _Obs_: End-point criado apenas para demonstrar o relacionamento entre User e Role.

#### [GET] /roles
> Para ver a lista de cargos cadastrados

#### [GET] /roles/<role_id>
> Para ver os dados do cargo de id igual a _role_id_

#### [POST] /roles
> Para incluir um novo cargo
> ```
> {
>     "authority": "SUPER_ADMIN"
> }
> ```

#### [DELETE] /roles/<role_id>
> Para excluir o registro do cargo de id igual a _role_id_
