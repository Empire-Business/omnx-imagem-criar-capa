---
name: omnx-imagem-criar-capa
description: "Preenche um molde de capa e entrega o prompt pronto para gerar a imagem, em quatro formatos: capa de curso, módulo, mentoria ou evento com protagonista; capa de plataforma com o print da tela; thumbnail de vídeo; flyer impresso de frente e verso. Use quando pedirem 'faz a capa do meu curso', 'capa do módulo', 'capa da plataforma com o print', 'thumbnail desse vídeo', 'arte de capa 16:9', 'key art', 'flyer do evento'. Cada capa sai com as mesmas seções, sem campo em branco e com o teste da miniatura. Não traz logo, cores ou marca prontos: usa os da pessoa, se ela tiver. Só escreve o prompt: não gera o arquivo. Não use para imagens sem molde, como foto de produto, post ou ilustração (omnx-imagem-criar-prompt), vídeo (omnx-video-criar-prompt), identidade visual, site ou slides (morfo)."
---

# Criar capa

Escolhe um dos quatro moldes, preenche todos os campos com decisões específicas e entrega o prompt pronto para colar na ferramenta de imagem da pessoa. O molde é sempre o mesmo para a ferramenta receber a informação na mesma ordem. O trabalho está em escolher bem o que entra em cada campo. Não gera a imagem.

## Como conversar

Quem usa pode nunca ter gerado uma imagem. Se a pessoa chegar sem contexto, diga em duas linhas o que você faz e pergunte para que é a capa. Uma pergunta por vez. Palavra técnica vem com meia frase de explicação. Toda resposta termina com o próximo passo. A pessoa nunca precisa digitar comando.

## Passos

1. **Escolha o molde.** Se o pedido não deixar claro, pergunte.

   | Para quê | Molde |
   |---|---|
   | Curso, módulo, mentoria, aula, evento, com pessoa ou personagem | `templates/molde-curso.md` |
   | Plataforma, sistema, app, painel, com o print da tela | `templates/molde-plataforma.md` |
   | Thumbnail de vídeo | `templates/molde-thumbnail.md` |
   | Flyer impresso, frente e verso | `templates/molde-flyer.md` |

2. **Colha o essencial.** Tema, título exato, e o que a pessoa vai anexar: foto, logo ou print. Pergunte se ela tem cores próprias. Se não tiver, você propõe a partir do assunto e declara. Plataforma: sem o print, avise que a capa depende dele. Flyer: use só os dados que ela der; sem eles, tire o bloco. Pergunte apenas o que muda a imagem inteira.
3. **Confira a ferramenta na documentação atual.** Busque na página oficial: aceita anexar imagens? Como trata texto dentro da imagem? Como pede a proporção? Em que idioma recebe melhor? Anote o link e a data. Só conta a documentação oficial: blog, fórum e vídeo não servem. Se o que ela diz depender da versão, pergunte a versão uma vez; sem resposta, diga no pacote para qual versão cada coisa vale. Não escreva tamanho em pixels, parâmetro ou versão de memória: mudam. Sem acesso ou sem resposta clara, entregue sem parâmetros e diga "não conferi os parâmetros desta ferramenta".
4. **Decida cada campo** com `references/como-preencher.md`, que diz onde cada campo costuma ficar genérico.
5. **Preencha o molde inteiro.** Copie o texto do molde, substitua todo colchete e mantenha as seções na ordem. Linhas marcadas com `[SE ...]` são para ser substituídas ou apagadas. Só traduza o molde se a documentação pedir, mantendo a ordem; o título fica sempre no idioma da peça.
6. **Confira com o script.** Salve o molde preenchido num arquivo temporário e rode, a partir da pasta deste `SKILL.md`:

   ```
   python3 scripts/conferir_molde.py templates/molde-<tipo>.md <preenchido.md>
   ```

   Ele devolve um JSON: `ok`, `secoes_faltando`, `fora_de_ordem`, `colchetes`. Se `ok` for `false`, corrija e rode de novo. Se traduziu o molde, acrescente `--so-colchetes`.
7. **Faça o teste da miniatura.** Imagine a capa do tamanho de uma unha. Sobrou uma ideia só, um foco só e um título que dá para ler? Se não, corte elementos antes de entregar.
8. **Entregue no formato abaixo**, na conversa. Salve em arquivo só se a pessoa pedir, no lugar que ela indicar.

## Regras

- **Sem marca de terceiro como estilo.** Nada de "como a capa de tal plataforma ou tal filme", nem logo de outra empresa.
- **Sem marca embutida.** Este molde não tem logo, paleta, fonte ou nome fixos. Logo só se a pessoa anexar, e ela é reproduzida exatamente como veio.
- **Foto de pessoa** só com autorização dela, dita na conversa. Nunca figura pública. Sem foto, descreva um personagem fictício.
- **Print:** antes de entregar, lembre a pessoa de conferir se aparece nome de cliente, e-mail, telefone ou valor. A capa circula muito.
- **A tela é documento.** Na capa de plataforma, nada é inventado dentro da interface. Elemento de curiosidade fica fora da tela.
- **Não invente dados do flyer:** preço, garantia, bônus, depoimento, resultado. QR code nunca é pedido à ferramenta de imagem: reserve o espaço e a pessoa coloca o código real em editor.

## Formato de entrega

```
**Capa: <nome>**
<molde preenchido por inteiro, em bloco de código>

**Como usar:** cole na sua ferramenta de imagem<, anexando nesta ordem: 1) ..., 2) ...>. <Proporção: como a documentação manda; sem documentação, peça em palavras a proporção do molde e diga para recortar depois, se vier outra.>
**Atenção:** <uma linha: o ponto mais provável de falhar nesta capa>
**Documentação:** <link e data, ou "não conferi os parâmetros desta ferramenta">

Próximo passo: <o que a pessoa faz agora>
```

Flyer: dois blocos, frente e verso.

Título que sai com letras erradas é comum em geradores de imagem. Nesse caso, peça a imagem sem texto (cada molde diz como) e oriente a pessoa a escrever o título em editor.

## Outro sistema operacional

O único script é `scripts/conferir_molde.py`, em Python 3 só com biblioteca padrão. Adapte o que for preciso e conte à pessoa o que realmente testou.

- **Python:** `python3` no macOS e Linux; `py -3` ou `python` no Windows. Sem Python, peça autorização para instalar pelo gerenciador oficial (Homebrew, winget, apt) ou faça a conferência do passo 6 à mão: todas as seções do molde presentes, na ordem, nenhum colchete sobrando.
- **Instalar:** no Windows, copie esta pasta, sem o `install.sh`, para `%USERPROFILE%\.claude\skills\omnx-imagem-criar-capa`. No Mac e no Linux, rode o `install.sh`.
- **Caminhos:** `~` é a pasta do usuário; no Windows é `%USERPROFILE%`. Caminho com espaço vai entre aspas.
- **Abrir um arquivo salvo para a pessoa:** `open` (macOS), `start ""` (Windows), `xdg-open` (Linux).

## Outra ferramenta (Codex e outras)

Compatível com Claude Code, Codex e outras ferramentas de agentes, em Mac, Windows e Linux. Se a pessoa pedir para instalar
fora do Claude Code, a IA dela adapta na hora, testa no computador dela e conta o que realmente funcionou:
- **Onde pôr os arquivos:** confira na documentação atual da ferramenta. No Codex, a referência em 08/11/2026 era `~/.agents/skills/<name>`.
- **Caminhos:** `templates/...`, `references/...` e `scripts/...` são relativos à pasta onde este `SKILL.md` ficou instalado.
- **Sem executar scripts:** faça a conferência do passo 6 à mão.
- **Pesquisa na internet:** se a ferramenta não pesquisar, siga o passo 3 como "sem acesso".
