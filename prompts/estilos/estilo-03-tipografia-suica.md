# Estilo 03 — Pôster suíço com tipografia cinética

- **Visual:** Estilo Tipográfico Internacional: uma palavra grotesca enorme numa grade rígida, um disco vermelho, fios finos.
- **Movimento:** as letras sobem de uma máscara na linha de base, o peso delas ondula numa onda que viaja, o disco pula pela grade na batida.

**Cinco regras:** (1) tudo encaixa numa grade de 12 colunas, nada flutua; (2) uma palavra enorme, apertada (tracking −2%), alinhada à esquerda na linha de base; (3) o disco vermelho é a única cor, o resto é tinta; (4) as letras entram de uma máscara na base, escalonadas 60 ms, quint-out; (5) o peso É o movimento: uma onda de 260 a 860 percorre a palavra.

```
R — REFERÊNCIAS
• O Estilo Tipográfico Internacional (design suíço): grades rígidas, equilíbrio assimétrico, uma cor forte.
• Animações de "onda de peso" com fonte variável (busque: variable font kinetic typography).
• Copie a disciplina, não os layouts.

I — IDEIA
Uma imagem, contada em 5 segundos, em loop sem costura:
• Início (0–1,3 s): uma grade vazia com um disco vermelho; a palavra "Motion" sobe letra por letra de uma máscara na linha de base.
• Meio (1,3–3,9 s): a palavra se mantém enquanto uma onda de peso percorre as letras; o disco pula para uma nova posição da grade a cada batida.
• Fim (3,9–5 s): as letras saem pelo topo da máscara, o fio se recolhe e o quadro volta a como começou.

S — ESTILO
Visual: fundo #0f0f0e, texto e fios #f1eee7, um disco #ff3b1f. Inter, pesada, tracking −2%, alinhada à esquerda numa grade de 12 colunas com margens generosas. Legendas minúsculas na mesma família.
Movimento: entradas quint-out escalonadas em 60 ms, uma onda de peso senoidal (260 a 860, duas ondas por loop), movimentos do disco de 0,7 s travados na batida. Ease-in e ease-out, nunca linear.
Regras:
1. Todo elemento está na grade: colunas, linha de base, margens.
2. Uma palavra enorme; ocupa cerca de 85% da largura da grade.
3. O disco é a única cor.
4. As letras entram de uma máscara na linha de base, escalonadas; saem do mesmo jeito, para cima.
5. A onda de peso é o movimento; posições só mudam nas entradas e saídas.
6. Grão e uma queda de luz suave para o fundo nunca ficar chapado.
7. Mantenha a palavra inteira na tela por pelo menos 1,2 s.

E — EXAMINAR
Construa um único arquivo HTML: um <canvas> e uma função pura render(ctx, t, theme, w, h) que desenha o frame t (0–5 s) a partir de theme {bg, ink, accent, accent2, font}. Mesmo t, mesmo frame, em qualquer ordem; hash com semente, sem Math.random. Precisa funcionar em 16:9, 9:16 e 1:1.
Renderize 5 frames (t = 0; 1,25; 2,5; 3,75; 5). Confira: o frame 0 é igual ao frame 5; a palavra cabe sem letras cortadas; o disco pousa exatamente nos pontos da grade; as legendas nunca colidem com a palavra; a onda de peso se lê como uma onda suave única. Corrija o que falhar e renderize de novo até todas as checagens passarem.
```
