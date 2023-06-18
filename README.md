# Code challenge DigitalSys

## Rodando o projeto com Docker

- Faça o [download](https://www.docker.com/products/docker-desktop/) e instale o Docker
- Inicie o docker desktop
- Inicie o container
```
# No CMD digite:

docker-compose up --build
```

A aplicação está rodando na porta: `8000`
- Acesse pelo [link](http://localhost:8000/)

Criação dos campos do formulário da proposta
- Acesse o [painel de admin](http://localhost:8000/admin/) da aplicação
- Realize o login com as credenciais `user: admin | senha: admin`
- Clique no menu `Fields` :

![fields](https://github.com/MauMaykot/digitalsys-code-challenge/assets/76183106/f68a2641-f3bf-43d5-99e8-3382860b2e1d)
- Se preferir exclua/edite os campos gerados automaticamente ou [adicione](http://localhost:8000/admin/proposal/field/add/) um novo campo:

![image](https://github.com/MauMaykot/digitalsys-code-challenge/assets/76183106/25185f1e-7b9f-42b1-957a-7da09e3039c4)
- Escolha o nome do campo e o tipo se for: Checkbox, Lista ou Seleção única crie suas opções:

![choices](https://github.com/MauMaykot/digitalsys-code-challenge/assets/76183106/d26021b5-2e00-4788-a7d8-f56a4e2305c4)
