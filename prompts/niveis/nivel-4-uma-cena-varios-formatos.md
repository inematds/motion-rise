# Nível 4 — Uma cena em todos os formatos

Uma única cena com layout próprio para 16:9, 9:16 e 1:1 — a composição inteira visível em cada um.
Onde usar: a mesma peça para vídeo horizontal, stories/vertical, feed quadrado e anúncios.

```
R: A minha narração termina com: "Com café suficiente, tudo é possível."
I: Uma xícara de café cujo vapor desenha uma tela de vídeo, uma tela de fotos e um post curto, cada uma com uma pequena cena viva, e depois volta a se enrolar para dentro da xícara.
S: Visual editorial escuro com luz quente de café. Movimento suave, 10 segundos, e o último frame é igual ao primeiro. UMA cena que se reorganiza para 16:9, 9:16 e 1:1 (nunca um recorte). Coloque const BEBIDA = 'café' no topo para eu poder trocar.
E: Desenhe todos os frames em código a partir de uma única função render(t). Adicione textura real para parecer feito à mão. Antes de terminar, confira os frames em 0%, 25%, 50%, 75% e 100% e corrija o que estiver errado.
```

**Recortar × reorganizar:** recortar corta as bordas da mesma cena; reorganizar monta uma composição nova para cada proporção, com a mesma ideia. O `const BEBIDA` mostra outro truque: deixar um parâmetro no topo do código para reaproveitar a peça.
