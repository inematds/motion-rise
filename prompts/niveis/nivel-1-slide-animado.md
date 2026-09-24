# Nível 1 — Um slide que se move sozinho

Loop de 10 s: um feixe de luz percorre uma linha do tempo e acende três marcos.
Onde usar: apresentações, aulas, relatórios, timelines, processos.

```
R: Aqui está o meu slide (screenshot anexado).
I: Um loop de 10 segundos que explica a ideia do slide: um feixe de luz percorre uma linha do tempo e acende três marcos.
S: Visual: papel marfim, linhas em tinta preta, um único destaque laranja-argila. Movimento lento e suave; o último frame é igual ao primeiro. 1920x1080.
E: Desenhe todos os frames em código a partir de uma única função render(t). Adicione textura real para parecer feito à mão. Antes de terminar, confira os frames em 0%, 25%, 50%, 75% e 100% e corrija o que estiver errado.
```

**Por que funciona:** o R prende a composição ao slide real; o I tem uma única transformação (o feixe); o S limita a paleta de propósito; o E obriga o modelo a olhar o próprio resultado.
