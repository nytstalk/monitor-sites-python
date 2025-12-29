# Monitor Universal de Sites

Script em Python desenvolvido para o monitoramento automatizado de alterações em websites. O projeto utiliza a biblioteca `undetected-chromedriver` para simular uma sessão de navegação humana, permitindo o acesso a páginas protegidas por sistemas anti-bot (como Cloudflare e captchas).

Quando uma alteração é detectada, o sistema emite um alerta sonoro nativo (Windows) e envia uma notificação push via Telegram com o horário do evento.

## Funcionalidades

* **Bypass de Proteções:** Utiliza uma instância real do Google Chrome para transpor verificações Cloudflare V2 e telas de "I'm under attack".
* **Integração Telegram:** Envio de alertas diretos para chat privado ou canais.
* **Modos de Monitoramento:**
    * **Página Completa:** Monitora alterações em todo o corpo HTML (`<body>`).
    * **Fórum Inteligente:** Tenta isolar containers de postagens comuns em softwares de fórum (XenForo, vBulletin, IPB) para reduzir falsos positivos causados por elementos dinâmicos (relógios, contadores de usuários).
* **Auto-Reparo:** Mecanismo que verifica e tenta instalar dependências ausentes na primeira execução.

## Pré-requisitos

* **Sistema Operacional:** Windows (Recomendado para suporte aos alertas de áudio nativos).
* **Navegador:** Google Chrome (Versão estável atualizada).
* **Python:** Versões 3.10, 3.11 ou 3.12.
    * *Nota: O Python 3.14 (Alpha) não é suportado devido à remoção do módulo `distutils`.*

## Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/nytstalk/monitor-sites-python.git](https://github.com/nytstalk/monitor-sites-python.git)
    cd monitor-sites-python
    ```

2.  Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
    *Caso utilize a instalação manual:*
    ```bash
    pip install undetected-chromedriver selenium
    ```
## Utilização

Execute o script através do terminal ou utilizando o arquivo `iniciar.bat`:

```bash
python main.py