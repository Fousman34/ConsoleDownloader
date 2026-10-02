"""Complete seven-language interface; rows have one translation per language."""
LANGUAGES = {
    'ru': 'Русский', 'en': 'English', 'es': 'Español', 'pt': 'Português',
    'fr': 'Français', 'de': 'Deutsch', 'zh': '中文（简体）',
}
# key | ru | en | es | pt | fr | de | zh
_ROWS = '''
app_name|Video Downloader|Video Downloader|Video Downloader|Video Downloader|Video Downloader|Video Downloader|Video Downloader
app_tagline|Видео с поддерживаемых сайтов и по прямым ссылкам|Videos from supported websites and direct links|Vídeos de sitios compatibles y enlaces directos|Vídeos de sites compatíveis e links diretos|Vidéos de sites compatibles et liens directs|Videos von unterstützten Websites und direkten Links|下载受支持网站的视频及直接链接视频
first_run|Выберите язык|Choose your language|Elige tu idioma|Escolha seu idioma|Choisissez votre langue|Sprache auswählen|请选择语言
choose_language|Язык интерфейса|Interface language|Idioma de la interfaz|Idioma da interface|Langue de l’interface|Sprache der Oberfläche|界面语言
menu_title|Главное меню|Main menu|Menú principal|Menu principal|Menu principal|Hauptmenü|主菜单
menu_download|📥 Скачать видео|📥 Download video|📥 Descargar vídeo|📥 Baixar vídeo|📥 Télécharger une vidéo|📥 Video herunterladen|📥 下载视频
menu_settings|⚙ Настройки|⚙ Settings|⚙ Ajustes|⚙ Configurações|⚙ Paramètres|⚙ Einstellungen|⚙ 设置
menu_about|ℹ О программе|ℹ About|ℹ Acerca de|ℹ Sobre|ℹ À propos|ℹ Über das Programm|ℹ 关于
menu_exit|Выход|Exit|Salir|Sair|Quitter|Beenden|退出
download_title|Скачать видео|Download video|Descargar vídeo|Baixar vídeo|Télécharger une vidéo|Video herunterladen|下载视频
prompt_url|Вставьте ссылку на страницу с видео или видеофайл|Paste a video page or direct media URL|Pega un enlace a una página de vídeo o archivo|Cole um link de página de vídeo ou arquivo|Collez le lien d’une page vidéo ou d’un fichier|Link zur Videoseite oder Videodatei einfügen|粘贴视频页面或视频文件链接
err_download_title|Это видео скачать не удалось|This video could not be downloaded|No se pudo descargar este vídeo|Não foi possível baixar este vídeo|Impossible de télécharger cette vidéo|Dieses Video konnte nicht heruntergeladen werden|无法下载此视频
err_url_empty|Ссылка не может быть пустой.|URL cannot be empty.|El enlace no puede estar vacío.|O link não pode estar vazio.|Le lien ne peut pas être vide.|Der Link darf nicht leer sein.|链接不能为空。
err_url_invalid|Нужна корректная ссылка HTTP или HTTPS. Проверьте адрес.|Enter a valid HTTP or HTTPS URL.|Introduce un enlace HTTP o HTTPS válido.|Insira um link HTTP ou HTTPS válido.|Saisissez un lien HTTP ou HTTPS valide.|Einen gültigen HTTP- oder HTTPS-Link eingeben.|请输入有效的 HTTP 或 HTTPS 链接。
prompt_quality|Выберите качество|Choose quality|Elige la calidad|Escolha a qualidade|Choisissez la qualité|Qualität auswählen|选择画质
q_360|360p|360p|360p|360p|360p|360p|360p
q_480|480p|480p|480p|480p|480p|480p|480p
q_720|720p · HD|720p · HD|720p · HD|720p · HD|720p · HD|720p · HD|720p · 高清
q_1080|1080p · Full HD|1080p · Full HD|1080p · Full HD|1080p · Full HD|1080p · Full HD|1080p · Full HD|1080p · 全高清
q_1440|1440p · 2K|1440p · 2K|1440p · 2K|1440p · 2K|1440p · 2K|1440p · 2K|1440p · 2K
q_2160|2160p · 4K|2160p · 4K|2160p · 4K|2160p · 4K|2160p · 4K|2160p · 4K|2160p · 4K
q_best|Лучшее доступное|Best available|Mejor disponible|Melhor disponível|Meilleure qualité disponible|Beste verfügbare Qualität|最佳可用画质
q_mp3|Только аудио · MP3|Audio only · MP3|Solo audio · MP3|Somente áudio · MP3|Audio uniquement · MP3|Nur Audio · MP3|仅音频 · MP3
downloading|Скачивание|Downloading|Descargando|Baixando|Téléchargement|Wird heruntergeladen|正在下载
processing|Обработка (FFmpeg)…|Processing (FFmpeg)…|Procesando (FFmpeg)…|Processando (FFmpeg)…|Traitement (FFmpeg)…|Verarbeitung (FFmpeg)…|正在处理 (FFmpeg)…
preparing|Получение информации…|Fetching information…|Obteniendo información…|Obtendo informações…|Récupération des informations…|Informationen werden abgerufen…|正在获取信息…
done_title|Готово!|Done!|¡Listo!|Pronto!|Terminé !|Fertig!|完成！
title_label|Название|Title|Título|Título|Titre|Titel|标题
duration_label|Длительность|Duration|Duración|Duração|Durée|Dauer|时长
saved_to|Сохранено в|Saved to|Guardado en|Salvo em|Enregistré dans|Gespeichert unter|保存位置
err_generic_title|Ошибка приложения|Application error|Error de la aplicación|Erro do aplicativo|Erreur de l’application|Anwendungsfehler|应用程序错误
err_hint_ytdlp|Обновите зависимости: python -m pip install -U "yt-dlp[default]". Для EXE нужна пересборка.|Update dependencies: python -m pip install -U "yt-dlp[default]". Rebuild the EXE afterwards.|Actualiza: python -m pip install -U "yt-dlp[default]". Después recompila el EXE.|Atualize: python -m pip install -U "yt-dlp[default]". Depois recompile o EXE.|Mettez à jour : python -m pip install -U "yt-dlp[default]". Recompilez ensuite l’EXE.|Aktualisieren: python -m pip install -U "yt-dlp[default]". Danach EXE neu erstellen.|更新依赖：python -m pip install -U "yt-dlp[default]"，然后重新构建 EXE。
err_hint_ffmpeg|Установите FFmpeg и добавьте его в PATH.|Install FFmpeg and add it to PATH.|Instala FFmpeg y añádelo a PATH.|Instale FFmpeg e adicione ao PATH.|Installez FFmpeg et ajoutez-le au PATH.|FFmpeg installieren und zum PATH hinzufügen.|安装 FFmpeg 并将其添加到 PATH。
cancel|Отменено.|Cancelled.|Cancelado.|Cancelado.|Annulé.|Abgebrochen.|已取消。
press_enter|Enter — вернуться в меню|Press Enter to return to menu|Pulsa Enter para volver al menú|Pressione Enter para voltar ao menu|Entrée pour revenir au menu|Enter drücken, um zum Menü zurückzukehren|按 Enter 返回菜单
settings_title|Настройки|Settings|Ajustes|Configurações|Paramètres|Einstellungen|设置
setting_lang|Язык интерфейса|Interface language|Idioma de la interfaz|Idioma da interface|Langue de l’interface|Sprache der Oberfläche|界面语言
setting_quality|Качество по умолчанию|Default quality|Calidad predeterminada|Qualidade padrão|Qualité par défaut|Standardqualität|默认画质
setting_folder|Папка для скачивания|Download folder|Carpeta de descargas|Pasta de downloads|Dossier de téléchargement|Downloadordner|下载文件夹
setting_proxy|Прокси|Proxy|Proxy|Proxy|Proxy|Proxy|代理
setting_cookies|Файл cookies.txt|Cookies.txt file|Archivo cookies.txt|Arquivo cookies.txt|Fichier cookies.txt|Cookies.txt-Datei|cookies.txt 文件
prompt_proxy|Адрес прокси (пусто — отключить)|Proxy URL (empty to disable)|URL del proxy (vacío para desactivar)|URL do proxy (vazio para desativar)|Adresse du proxy (vide pour désactiver)|Proxy-URL (leer zum Deaktivieren)|代理地址（留空禁用）
prompt_cookies|Путь к cookies.txt Netscape (пусто — отключить)|Netscape cookies.txt path (empty to disable)|Ruta a cookies.txt Netscape (vacío para desactivar)|Caminho de cookies.txt Netscape (vazio para desativar)|Chemin de cookies.txt Netscape (vide pour désactiver)|Pfad zu Netscape cookies.txt (leer zum Deaktivieren)|Netscape cookies.txt 路径（留空禁用）
back|← Назад|← Back|← Volver|← Voltar|← Retour|← Zurück|← 返回
folder_prompt|Путь к папке (Tab — автодополнение)|Folder path (Tab to autocomplete)|Ruta de carpeta (Tab para completar)|Caminho da pasta (Tab para completar)|Chemin du dossier (Tab pour compléter)|Ordnerpfad (Tab zum Vervollständigen)|文件夹路径（Tab 自动补全）
folder_current|Текущая папка|Current folder|Carpeta actual|Pasta atual|Dossier actuel|Aktueller Ordner|当前文件夹
quality_current|Качество по умолчанию|Default quality|Calidad predeterminada|Qualidade padrão|Qualité par défaut|Standardqualität|默认画质
lang_current|Текущий язык|Current language|Idioma actual|Idioma atual|Langue actuelle|Aktuelle Sprache|当前语言
saved|Сохранено|Saved|Guardado|Salvo|Enregistré|Gespeichert|已保存
updated|Настройка обновлена|Setting updated|Ajuste actualizado|Configuração atualizada|Paramètre mis à jour|Einstellung aktualisiert|设置已更新
about_title|О программе|About|Acerca de|Sobre|À propos|Über das Programm|关于
about_text|[bold]Video Downloader[/] — видео и MP3 с поддерживаемых сайтов и по прямым ссылкам. Качество до 4K, прогресс, папка, прокси и cookies. Стрелки — выбор, Enter — подтвердить, Tab — путь, Ctrl+C — отмена. DRM и некоторые сайты не поддерживаются.|[bold]Video Downloader[/] — video and MP3 from supported websites and direct links. Quality up to 4K, progress, folder, proxy and cookies. Arrows to select, Enter to confirm, Tab for paths, Ctrl+C to cancel. DRM and some websites are unsupported.|[bold]Video Downloader[/] — vídeo y MP3 de sitios compatibles y enlaces directos. Hasta 4K, progreso, carpeta, proxy y cookies. Flechas para elegir, Enter para confirmar, Tab para rutas, Ctrl+C para cancelar. DRM y algunos sitios no son compatibles.|[bold]Video Downloader[/] — vídeo e MP3 de sites compatíveis e links diretos. Até 4K, progresso, pasta, proxy e cookies. Setas para escolher, Enter para confirmar, Tab para caminhos, Ctrl+C para cancelar. DRM e alguns sites não são compatíveis.|[bold]Video Downloader[/] — vidéo et MP3 de sites compatibles et liens directs. Jusqu’à 4K, progression, dossier, proxy et cookies. Flèches pour choisir, Entrée pour confirmer, Tab pour les chemins, Ctrl+C pour annuler. DRM et certains sites ne sont pas pris en charge.|[bold]Video Downloader[/] — Video und MP3 von unterstützten Websites und direkten Links. Bis 4K, Fortschritt, Ordner, Proxy und Cookies. Pfeile zur Auswahl, Enter zum Bestätigen, Tab für Pfade, Ctrl+C zum Abbrechen. DRM und manche Websites werden nicht unterstützt.|[bold]Video Downloader[/] — 下载受支持网站及直接链接的视频和 MP3。最高 4K，支持进度、文件夹、代理和 cookies。方向键选择，Enter 确认，Tab 补全路径，Ctrl+C 取消。不支持 DRM 及部分网站。
goodbye|До встречи!|See you!|¡Hasta luego!|Até logo!|À bientôt !|Bis bald!|再见！
select_help|(↑/↓ — выбор, Enter — подтвердить)|(↑/↓ to select, Enter to confirm)|(↑/↓ para elegir, Enter para confirmar)|(↑/↓ para escolher, Enter para confirmar)|(↑/↓ pour choisir, Entrée pour confirmer)|(↑/↓ zur Auswahl, Enter zum Bestätigen)|(↑/↓ 选择，Enter 确认)
menu_doctor|Проверка зависимостей|Check dependencies|Comprobar dependencias|Verificar dependências|Vérifier les dépendances|Abhängigkeiten prüfen|检查依赖
err_quality|Неподдерживаемое качество.|Unsupported quality.|Calidad no compatible.|Qualidade não compatível.|Qualité non prise en charge.|Nicht unterstützte Qualität.|不支持的画质。
err_ffmpeg|Нужны ffmpeg и ffprobe. Установите FFmpeg или используйте готовую сборку.|ffmpeg and ffprobe are required. Install FFmpeg or use the portable build.|Se necesitan ffmpeg y ffprobe. Instala FFmpeg o usa la versión portátil.|ffmpeg e ffprobe são necessários. Instale FFmpeg ou use a versão portátil.|ffmpeg et ffprobe sont requis. Installez FFmpeg ou utilisez la version portable.|ffmpeg und ffprobe werden benötigt. FFmpeg installieren oder portable Version verwenden.|需要 ffmpeg 和 ffprobe。请安装 FFmpeg 或使用便携版。
err_js|Для некоторых сайтов нужен Node.js 22+ или Deno 2.3+.|Some websites require Node.js 22+ or Deno 2.3+.|Algunos sitios necesitan Node.js 22+ o Deno 2.3+.|Alguns sites precisam de Node.js 22+ ou Deno 2.3+.|Certains sites nécessitent Node.js 22+ ou Deno 2.3+.|Manche Websites benötigen Node.js 22+ oder Deno 2.3+.|部分网站需要 Node.js 22+ 或 Deno 2.3+。
err_cookies|Файл cookies.txt не найден.|Cookies.txt file was not found.|No se encontró cookies.txt.|Arquivo cookies.txt não encontrado.|Fichier cookies.txt introuvable.|Cookies.txt-Datei nicht gefunden.|找不到 cookies.txt 文件。
err_no_file|Загрузка не создала итоговый файл. Попробуйте обновить yt-dlp.|No final file was created. Try updating yt-dlp.|No se creó un archivo final. Actualiza yt-dlp.|Nenhum arquivo final foi criado. Atualize yt-dlp.|Aucun fichier final créé. Essayez de mettre à jour yt-dlp.|Keine fertige Datei erstellt. yt-dlp aktualisieren.|未生成最终文件。请尝试更新 yt-dlp。
err_config|Ошибка настроек|Settings error|Error de ajustes|Erro de configurações|Erreur des paramètres|Einstellungsfehler|设置错误
config_fallback|Используются настройки по умолчанию. Исходный файл пока не изменён.|Using defaults. The original file has not been changed yet.|Se usan valores predeterminados. El archivo original aún no se ha modificado.|Usando padrões. O arquivo original ainda não foi alterado.|Valeurs par défaut utilisées. Le fichier original n’a pas encore été modifié.|Standardwerte werden verwendet. Die Originaldatei wurde noch nicht geändert.|使用默认设置，原文件尚未更改。
err_terminal|Для меню нужен интерактивный терминал. Запустите start.cmd или передайте URL в командной строке.|The menu requires an interactive terminal. Run start.cmd or pass a URL on the command line.|El menú necesita un terminal interactivo. Ejecuta start.cmd o pasa un enlace por la línea de comandos.|O menu precisa de terminal interativo. Execute start.cmd ou informe um URL na linha de comando.|Le menu nécessite un terminal interactif. Lancez start.cmd ou passez un lien en ligne de commande.|Das Menü benötigt ein interaktives Terminal. start.cmd starten oder URL als Argument angeben.|菜单需要交互式终端。运行 start.cmd 或在命令行传入链接。
error_help|Проверьте интернет и зависимости (--doctor). При необходимости задайте прокси или cookies. Подробнее: README.md.|Check your connection and dependencies (--doctor). Configure proxy or cookies if needed. See README.md.|Comprueba conexión y dependencias (--doctor). Configura proxy o cookies si hace falta. Consulta README.md.|Verifique conexão e dependências (--doctor). Configure proxy ou cookies se necessário. Veja README.md.|Vérifiez connexion et dépendances (--doctor). Configurez proxy ou cookies si nécessaire. Voir README.md.|Verbindung und Abhängigkeiten prüfen (--doctor). Bei Bedarf Proxy oder Cookies einstellen. Siehe README.md.|检查网络和依赖 (--doctor)，必要时配置代理或 cookies。详见 README.md。
err_collection|Это список видео. Вставьте ссылку на отдельный ролик.|This is a video collection. Paste an individual video URL.|Es una lista de vídeos. Pega el enlace de un vídeo individual.|É uma lista de vídeos. Cole o link de um vídeo individual.|Il s’agit d’une liste de vidéos. Collez le lien d’une vidéo individuelle.|Dies ist eine Videosammlung. Link zu einem einzelnen Video eingeben.|这是视频列表，请输入单个视频的链接。
err_live|Прямая трансляция ещё идёт. Дождитесь записи трансляции.|This broadcast is still live. Wait for the recording.|La transmisión sigue en directo. Espera a la grabación.|A transmissão ainda está ao vivo. Aguarde a gravação.|La diffusion est encore en direct. Attendez l’enregistrement.|Diese Übertragung läuft noch live. Auf die Aufzeichnung warten.|直播尚未结束，请等待录像。
err_media|Полученный файл не является ожидаемым видео или аудио. Он не отмечен как успешно скачанный.|The file is not the expected video or audio. It is not marked as a successful download.|El archivo no es el vídeo o audio esperado. No se considera una descarga correcta.|O arquivo não é o vídeo ou áudio esperado. Não é considerado um download concluído.|Le fichier n’est pas la vidéo ou l’audio attendu. Le téléchargement n’est pas validé.|Die Datei enthält nicht das erwartete Video oder Audio. Der Download gilt nicht als erfolgreich.|文件不是预期的视频或音频，不会标记为下载成功。
err_height|Разрешение файла выше выбранного предела. Выберите «Лучшее доступное», чтобы сохранить исходное качество.|The file exceeds the selected height limit. Choose Best available to keep the original quality.|La resolución supera el límite elegido. Elige Mejor disponible para conservar la calidad original.|A resolução excede o limite escolhido. Escolha Melhor disponível para manter a qualidade original.|La résolution dépasse la limite choisie. Sélectionnez Meilleure qualité disponible pour garder l’original.|Die Auflösung überschreitet die gewählte Grenze. Beste verfügbare Qualität wählen, um das Original zu behalten.|文件分辨率超出所选限制，选择最佳可用画质以保留原始画质。
err_disk|Не удалось сохранить файл. Проверьте папку, права доступа и свободное место.|Could not save the file. Check folder permissions and free disk space.|No se pudo guardar. Comprueba carpeta, permisos y espacio libre.|Não foi possível salvar. Verifique pasta, permissões e espaço livre.|Impossible d’enregistrer. Vérifiez dossier, droits et espace libre.|Datei konnte nicht gespeichert werden. Ordnerrechte und freien Speicher prüfen.|无法保存文件，请检查文件夹权限及可用磁盘空间。
err_drm|Видео защищено DRM. Это приложение не может его скачать.|This video is DRM protected. This application cannot download it.|El vídeo está protegido por DRM. Esta aplicación no puede descargarlo.|O vídeo é protegido por DRM. Este aplicativo não pode baixá-lo.|Cette vidéo est protégée par DRM. L’application ne peut pas la télécharger.|Dieses Video ist DRM-geschützt. Die Anwendung kann es nicht herunterladen.|此视频受 DRM 保护，本应用无法下载。
err_unsupported|Видео скачать не удастся: сайт не поддерживается или по ссылке не найдено видео.|Cannot download: the website is unsupported or no video was found at this URL.|No se puede descargar: el sitio no es compatible o no se encontró vídeo.|Não é possível baixar: site não compatível ou nenhum vídeo encontrado.|Téléchargement impossible : site non pris en charge ou aucune vidéo trouvée.|Download nicht möglich: Website wird nicht unterstützt oder kein Video gefunden.|无法下载：不支持该网站，或链接中未找到视频。
err_access|Сайт ограничил доступ. Возможно, нужны действующие cookies или доступ из вашего региона.|The website restricted access. Valid cookies or access from your region may be required.|El sitio restringió el acceso. Pueden necesitarse cookies válidas o acceso desde tu región.|O site restringiu o acesso. Cookies válidos ou acesso da sua região podem ser necessários.|Le site limite l’accès. Des cookies valides ou un accès depuis votre région peuvent être requis.|Die Website beschränkt den Zugriff. Gültige Cookies oder Zugang aus Ihrer Region können nötig sein.|网站限制了访问，可能需要有效 cookies 或所在地区的访问权限。
err_unavailable|Видео удалено, ссылка истекла или файл недоступен.|The video was removed, the link expired, or the file is unavailable.|El vídeo fue eliminado, el enlace caducó o el archivo no está disponible.|O vídeo foi removido, o link expirou ou o arquivo está indisponível.|La vidéo a été supprimée, le lien a expiré ou le fichier est indisponible.|Video gelöscht, Link abgelaufen oder Datei nicht verfügbar.|视频已删除、链接已过期或文件不可用。
err_format|Выбранное качество недоступно. Попробуйте другое или «Лучшее доступное».|Selected quality is unavailable. Try another quality or Best available.|La calidad elegida no está disponible. Prueba otra o Mejor disponible.|A qualidade escolhida não está disponível. Tente outra ou Melhor disponível.|La qualité choisie est indisponible. Essayez une autre ou Meilleure qualité disponible.|Gewählte Qualität nicht verfügbar. Andere Qualität oder Beste verfügbare Qualität versuchen.|所选画质不可用，请尝试其他画质或最佳可用画质。
err_network|Не удалось соединиться с сайтом. Проверьте интернет и попробуйте позже.|Could not connect to the website. Check your connection and try later.|No se pudo conectar al sitio. Comprueba internet e inténtalo más tarde.|Não foi possível conectar ao site. Verifique a internet e tente depois.|Connexion au site impossible. Vérifiez internet et réessayez plus tard.|Verbindung zur Website fehlgeschlagen. Internet prüfen und später erneut versuchen.|无法连接网站，请检查网络并稍后重试。
err_site|Не удалось скачать видео с этого сайта. Попробуйте обновить yt-dlp или другую ссылку.|Could not download from this website. Try updating yt-dlp or another URL.|No se pudo descargar de este sitio. Actualiza yt-dlp o prueba otro enlace.|Não foi possível baixar deste site. Atualize yt-dlp ou tente outro link.|Impossible de télécharger depuis ce site. Mettez à jour yt-dlp ou essayez un autre lien.|Download von dieser Website fehlgeschlagen. yt-dlp aktualisieren oder anderen Link versuchen.|无法从此网站下载，请更新 yt-dlp 或尝试其他链接。
error_details|Подробности сайта|Website details|Detalles del sitio|Detalhes do site|Détails du site|Details der Website|网站详细信息
config_label|Файл настроек|Settings file|Archivo de ajustes|Arquivo de configurações|Fichier de paramètres|Einstellungsdatei|设置文件
missing_tool|Не найден|Missing|No encontrado|Não encontrado|Introuvable|Nicht gefunden|未找到
broken_tool|Ошибка запуска|Failed to run|Error al ejecutar|Falha ao executar|Échec du lancement|Start fehlgeschlagen|运行失败
author_license|Автор: Fousman34 · Лицензия: GPLv3 · Исходники: github.com/Fousman34/ConsoleDownloader|Author: Fousman34 · License: GPLv3 · Source: github.com/Fousman34/ConsoleDownloader|Autor: Fousman34 · Licencia: GPLv3 · Código: github.com/Fousman34/ConsoleDownloader|Autor: Fousman34 · Licença: GPLv3 · Código: github.com/Fousman34/ConsoleDownloader|Auteur : Fousman34 · Licence : GPLv3 · Code : github.com/Fousman34/ConsoleDownloader|Autor: Fousman34 · Lizenz: GPLv3 · Quellcode: github.com/Fousman34/ConsoleDownloader|作者：Fousman34 · 许可证：GPLv3 · 源代码：github.com/Fousman34/ConsoleDownloader
cli_arguments|Аргументы|Arguments|Argumentos|Argumentos|Arguments|Argumente|参数
cli_options|Параметры|Options|Opciones|Opções|Options|Optionen|选项
cli_help|Показать справку и выйти|Show help and exit|Mostrar ayuda y salir|Mostrar ajuda e sair|Afficher l’aide et quitter|Hilfe anzeigen und beenden|显示帮助并退出
cli_version|Показать версию и выйти|Show version and exit|Mostrar versión y salir|Mostrar versão e sair|Afficher la version et quitter|Version anzeigen und beenden|显示版本并退出
license_notice|Без гарантий. Распространение разрешено по GPLv3; полный текст в LICENSE.|No warranty. Redistribution is permitted under GPLv3; see LICENSE.|Sin garantía. Se permite redistribuir bajo GPLv3; consulta LICENSE.|Sem garantia. Redistribuição permitida sob GPLv3; veja LICENSE.|Sans garantie. Redistribution autorisée sous GPLv3 ; voir LICENSE.|Ohne Gewährleistung. Weitergabe unter GPLv3 erlaubt; siehe LICENSE.|不提供保证。可按 GPLv3 再分发，完整条款见 LICENSE。
'''
TRANS = {code: {} for code in LANGUAGES}
for row in _ROWS.strip().splitlines():
    key, *values = row.split('|')
    if len(values) != len(LANGUAGES) or not all(values):
        raise ValueError('Incomplete translation: ' + key)
    for code, value in zip(LANGUAGES, values):
        TRANS[code][key] = value
_current = 'en'


def set_lang(code):
    global _current
    if code in TRANS:
        _current = code


def get_lang():
    return _current


def t(key):
    return TRANS[_current].get(key, key)
