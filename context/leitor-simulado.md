# Leitor simulado — 2026-09-24

Personas: confeiteira 34 (celular, intervalo) e corretor 58 (computador, à noite). Rodada única sobre as 10 aulas.

Notas da rodada: aulas 1–3 entre 7 e 9; 4 (5–6), 5 (4), 6 (6), 7 (6–7), 8 (6–7), 9 (6–7), 10 (6–7).

## Travas comuns e o que mudou
| Trava | Correção |
|---|---|
| Nenhuma aula ensina a tirar a peça do chat e postar | Aula 5 ganhou o step "Do chat para o post" (botão "baixar vídeo" + 2 contornos); aula 10 aponta para ele. Demo `exemplos/reel-legenda.html` testada: gera arquivo de 10 s 1080x1920 (container mp4, codec vp9 no Chromium — por isso o contorno do gravador de tela). |
| Aula 5 dependia de anexar vídeo e de "arquivo de legenda" sem nome | Caminho principal virou "texto falado + duração"; .srt foi para "Quer saber mais"; o vídeo entra por um botão "escolher vídeo" na própria página. |
| `const BEBIDA = 'café'` é código | Trocado por "deixe a palavra BEBIDA = café numa linha separada, no topo da receita" (aula 6 e nivel-4.md). |
| render(t) / 1920x1080 sem aviso | Aviso "instruções para a IA: copie sem mexer" na aula 1 (psafe), aula 2 (step 4) e na biblioteca. |
| Opus 5.5 pode não estar na conta | Aula 1: "use o modelo mais avançado da lista". |
| Link da biblioteca abria página técnica | Nova `biblioteca.html` (gerada por `scripts/gerar-biblioteca.py`) com botão copiar. |
| Faltam figuras reais | Aula 3: faixa de cinco quadros; aula 4: slide parado × quadro da animação; aula 5: reel rodando; aula 7: vinheta de logotipo com som rodando. |
| Sem site / no celular | Aula 4: print do perfil na rede social; aula 7: tocar e segurar › Salvar imagem; PNG serve. |
| "cartão Animação desenhada", "Style", "Newsreader", "palco vazio", "cor chapada", mapeamento de papéis da aula 10 | Reescritos. |

## Não feito (anotado)
- Miniaturas dos 6 estilos na aula 8 (só o 03 roda como demo).
- Par referência → resultado na aula 8 com imagens reais.
- Teste humano (TESTE-HUMANO §2) — pendente de pessoas.
