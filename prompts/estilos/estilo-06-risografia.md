# Estilo 06 — Risografia em duas cores

- **Visual:** duas tintas fluorescentes sobre papel preto: um sol listrado, um letreiro condensado gigante, grão, falhas e desregistro.
- **Movimento:** impresso a 12 quadros por segundo: o sol nasce e se põe, os letreiros deslizam em direções opostas, as chapas tremem fora de registro.

**Cinco regras:** (1) exatamente duas tintas; onde se sobrepõem viram uma terceira cor; (2) toda camada de tinta "imprime": pontinhos de falha e densidade irregular; (3) as duas chapas ficam levemente fora de registro e tremem a cada quadro; (4) animação "em dois": 12 quadros impressos por segundo, grão novo a cada quadro; (5) uma palavra condensada enorme, repetida como letreiro corrido.

```
R — REFERÊNCIAS
• Impressões e zines em risografia (busque: risograph two colour print, fluorescent pink riso).
• Animações stop-motion em riso: cada quadro impresso, o grão mudando de quadro a quadro.

I — IDEIA
Uma imagem com início, meio e fim, 5 segundos, em loop sem costura:
• Início (0–1,5 s): um sol listrado baixo no quadro; um letreiro condensado gigante com a palavra "Print" começa a deslizar sobre ele.
• Meio (1,5–3,5 s): o sol sobe através do letreiro; onde as tintas se sobrepõem, viram uma terceira cor; um segundo letreiro menor corre no sentido oposto.
• Fim (3,5–5 s): o sol se põe de volta onde começou e os dois letreiros pousam exatamente uma repetição adiante.

S — ESTILO
Visual: papel preto #111111 com fibras; tinta um #ff48b0, tinta dois #1f9bd1; Anton enorme e condensada; marcas de registro nos cantos.
Movimento: tudo anda em passos de 12 fps; os letreiros andam exatamente uma repetição por loop; as chapas tremem fora de registro uma fração de porcento a cada quadro impresso.
Regras:
1. Só duas tintas, misturadas em modo screen sobre o papel escuro.
2. Pontinhos de falha e densidade irregular em cada camada de tinta.
3. Desregistro: uma chapa deslocada e tremendo.
4. Movimento em passos de 12 fps; grão novo a cada quadro.
5. Listras ou grão no lugar de degradês.

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–5 s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0; 1,25; 2,5; 3,75; 5). Confira: o frame 0 é igual ao frame 5; exatamente duas tintas mais a sobreposição; o grão é visível em tamanho real; o letreiro dá a volta sem pulo; o desregistro é sutil, não parece quebrado. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
