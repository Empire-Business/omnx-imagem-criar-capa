# Capa

Guia visual: abra o `COMO-FUNCIONA.html` desta pasta (dois cliques; funciona sem internet).

Preenche um molde de capa e entrega o texto (prompt) pronto para gerar a imagem. Quatro moldes: capa de curso, módulo ou evento com protagonista; capa de plataforma com o print da tela; thumbnail de vídeo; flyer de frente e verso. Não tem logo, cores nem marca prontos. Não gera a imagem.

## Como instalar

**Direto do GitHub:** no Claude Code, diga: "Instale a skill a partir de https://github.com/Empire-Business/omnx-imagem-criar-capa". Para atualizar, diga: "Atualize a skill a partir de https://github.com/Empire-Business/omnx-imagem-criar-capa". A IA baixa e copia os arquivos.

Se você já baixou esta pasta:

1. Abra o Claude Code (aplicativo do Claude, aba **Code**, ambiente **Local**).
2. Escreva: **"Instale a skill omnx-imagem-criar-capa a partir desta pasta: `<caminho desta pasta>`"**.
3. A IA copia a skill para o lugar certo. Você não digita comando nenhum e vê um aviso de que terminou.
4. Abra uma conversa nova e peça, por exemplo: **"Faz a capa do meu curso de finanças para dentistas."**.

### Instalar à mão

- **Mac ou Linux:** rode `bash install.sh` nesta pasta (dá para rodar de qualquer lugar, com o caminho entre aspas). A skill vai para `~/.claude/skills/omnx-imagem-criar-capa`. Se editar algo aqui, rode de novo.
- **Windows:** copie esta pasta, sem o `install.sh`, para `%USERPROFILE%\.claude\skills\omnx-imagem-criar-capa`. Ou peça para a IA fazer isso.

## O que ela não faz

- Não gera o arquivo da imagem.
- Não imita a marca de outra empresa.
- Não inventa preço, bônus, depoimento nem conteúdo dentro da tela.
- Imagem sem molde é da `omnx-imagem-criar-prompt`; site e identidade visual, do Morfo.

## Pedidos que funcionam

- "Faz a capa do meu curso de finanças para dentistas."
- "Capa da minha plataforma com este print da tela."
- "Thumbnail para o vídeo sobre como organizar as contas."
- "Flyer de frente e verso para o meu evento."

## Outro sistema operacional e outra ferramenta

As seções "Outro sistema operacional" e "Outra ferramenta (Codex e outras)" do `SKILL.md` dizem à IA o que adaptar. Feita e testada no Claude Code em macOS. **Não foi testada no Codex** nem no Windows e Linux: a IA da pessoa adapta ao instalar e conta o que funcionou.
