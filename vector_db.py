#Generamos las importaciones necesarias
import pandas as pd #Pandas sirve para trabajar en formato de tablas la informacion
import chromadb #Es la estructura del proyecto siendo la base de datos de vectores (muy usada en chatbots, IA y RAG)
from sentence_transformers import SentenceTransformer #Complemento de la chromadb que convierte el texto en vectores
import os #Sirve para manejar archivos, carpetas y variables de entorno


# Cargamos todos nuestros datos , que en este caso son 100 de diferentes animes y personajes escogidos uno por uno jajajaja, no es mame
def cargar_datos_verificados():
    datos_verificados = [
        {'Anime': 'Shingeki No Kyojin', 'Personaje': 'Eren Yeager', 'biografia': 'Protagonista principal que busca la libertad y jura aniquilar a los Titanes después de que uno devorara a su madre. Posee el poder del Titán de Ataque, el Titán Fundador y el Titán Martillo de Guerra.'},
        {'Anime': 'Shingeki No Kyojin', 'Personaje': 'Mikasa Ackerman', 'biografia': 'Amiga de la infancia de Eren y una de las soldados más hábiles. Es extremadamente protectora con Eren y se une al Cuerpo de Exploración para seguirlo y protegerlo.'},
        {'Anime': 'Shingeki No Kyojin', 'Personaje': 'Armin Arlert', 'biografia': 'Amigo de la infancia de Eren y Mikasa, conocido por su gran inteligencia y capacidad estratégica. Hereda el poder del Titán Colosal y se convierte en un pilar para la humanidad.'},
        {'Anime': 'Shingeki No Kyojin', 'Personaje': 'Reiner Braun', 'biografia': 'Un soldado que actúa como figura de hermano mayor para los demás, pero que en realidad es el portador del Titán Acorazado. Lucha con un conflicto interno debido a su doble vida.'},
        {'Anime': 'Shingeki No Kyojin', 'Personaje': 'Sasha Blouse', 'biografia': 'Conocida como "la chica patata", es una miembro del Cuerpo de Exploración con un apetito voraz y habilidades excepcionales como cazadora. Aporta alivio cómico y es una experta arquera.'},
        {'Anime': 'Shingeki No Kyojin', 'Personaje': 'Levi Ackerman', 'biografia': 'El soldado más fuerte de la humanidad y capitán del Cuerpo de Exploración. Es famoso por su increíble habilidad en el combate y su personalidad fría y distante.'},
        {'Anime': 'Demon Slayer', 'Personaje': 'Tanjiro Kamado', 'biografia': 'Protagonista principal que se convierte en un cazador de demonios para vengar a su familia y encontrar una cura para su hermana, Nezuko. Es conocido por su gran corazón y su olfato sobrehumano.'},
        {'Anime': 'Demon Slayer', 'Personaje': 'Nezuko Kamado', 'biografia': 'La hermana menor de Tanjiro, convertida en demonio pero que se resiste a consumir humanos. Lucha junto a su hermano usando sus poderes demoníacos para proteger a los inocentes.'},
        {'Anime': 'Demon Slayer', 'Personaje': 'Inosuke Hashibira', 'biografia': 'Un cazador de demonios criado por jabalíes, caracterizado por su temperamento explosivo y su máscara de jabalí. Utiliza un estilo de lucha autodidacta con dos espadas serradas.'},
        {'Anime': 'Demon Slayer', 'Personaje': 'Zenitsu Agatsuma', 'biografia': 'Un cazador de demonios extremadamente cobarde que solo puede luchar cuando está inconsciente o dormido. A pesar de su miedo, es un maestro de la Respiración del Rayo.'},
        {'Anime': 'Demon Slayer', 'Personaje': 'Kyōjurō Rengoku', 'biografia': 'El Pilar de la Llama del Cuerpo de Cazadores de Demonios. Es un espadachín carismático y poderoso con un fuerte sentido de la justicia, que sirve de inspiración para Tanjiro.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Yuji Itadori', 'biografia': 'Protagonista que se convierte en el recipiente de Sukuna, el Rey de las Maldiciones, tras ingerir uno de sus dedos. Se une a la Escuela de Hechicería de Tokio para controlar su poder.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Satoru Gojo', 'biografia': 'Considerado el hechicero de Jujutsu más poderoso del mundo y maestro en la Escuela de Tokio. Es conocido por su técnica de los Seis Ojos y su personalidad despreocupada y juguetona.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Sukuna', 'biografia': 'El Rey de las Maldiciones, una entidad malévola y extremadamente poderosa que reside en el cuerpo de Yuji Itadori. Su objetivo es recuperar todo su poder y sembrar el caos.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Suguru Geto', 'biografia': 'Un antiguo amigo de Satoru Gojo y un poderoso hechicero que desertó para seguir un camino oscuro. Su objetivo es crear un mundo donde solo existan los hechiceros.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Nobara Kugisaki', 'biografia': 'Una hechicera de primer año y compañera de Yuji y Megumi, conocida por su fuerte carácter y su técnica de muñeco vudú. Proviene del campo y tiene una gran confianza en sí misma.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Megumi Fushiguro', 'biografia': 'Un hechicero de primer año que utiliza la técnica de las Diez Sombras para invocar shikigamis. Es un joven serio y calculador con un gran potencial latente.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Maki Zenin', 'biografia': 'Una estudiante de segundo año de la Escuela de Hechicería que nació sin energía maldita en el clan Zenin. Compensa su falta de poder con una habilidad física sobrehumana y maestría en armas.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Aoi Todo', 'biografia': 'Un estudiante de tercer año de la Escuela de Kioto con una fuerza física inmensa y una personalidad excéntrica. Considera a Yuji su "mejor amigo" y lo ayuda a crecer como hechicero.'},
        {'Anime': 'Jujutsu Kaisen', 'Personaje': 'Kento Nanami', 'biografia': 'Un hechicero de primer grado y antiguo asalariado que desprecia las horas extras. Es un mentor para Yuji, conocido por su técnica que le permite crear puntos débiles en sus enemigos.'},
        {'Anime': 'Boku no Hero Academia', 'Personaje': 'Izuku Midoriya', 'biografia': 'Protagonista que nace sin un "Don" en un mundo de superhéroes, pero hereda el poder One For All de su ídolo, All Might. Su sueño es convertirse en el mayor héroe de todos.'},
        {'Anime': 'Boku no Hero Academia', 'Personaje': 'Katsuki Bakugo', 'biografia': 'Rival de la infancia de Izuku, con un Don que le permite crear explosiones con el sudor de sus manos. Es arrogante y agresivo, pero increíblemente talentoso y decidido.'},
        {'Anime': 'Boku no Hero Academia', 'Personaje': 'Shoto Todoroki', 'biografia': 'Hijo del héroe número uno, Endeavor, que posee el Don de controlar tanto el hielo como el fuego. Inicialmente es frío y distante debido a su conflictivo pasado familiar.'},
        {'Anime': 'Boku no Hero Academia', 'Personaje': 'Toshinori Yagi', 'biografia': 'Conocido mundialmente como All Might, el Símbolo de la Paz. Es el antiguo portador del One For All y mentor de Izuku Midoriya, aunque una herida limita su tiempo como héroe.'},
        {'Anime': 'Boku no Hero Academia', 'Personaje': 'Shota Aizawa', 'biografia': 'Conocido como el héroe Eraser Head, es el profesor de la Clase 1-A en la Academia U.A. Su Don le permite anular los Dones de otros con solo mirarlos.'},
        {'Anime': 'Boku no Hero Academia', 'Personaje': 'Ochako Uraraka', 'biografia': 'Compañera de clase y amiga cercana de Izuku, cuyo Don es la Gravedad Cero. Su motivación para ser una heroína es poder darle una vida cómoda a sus padres.'},
        {'Anime': 'Bunny Girl Senpai', 'Personaje': 'Mai Sakurajima', 'biografia': 'Una famosa actriz adolescente que sufre del "Síndrome de la Pubertad", volviéndose invisible para los demás. Es la principal interés amoroso del protagonista, Sakuta Azusagawa.'},
        {'Anime': 'Bunny Girl Senpai', 'Personaje': 'Sakuta Azusagawa', 'biografia': 'Un estudiante de secundaria que ayuda a chicas que sufren del misterioso "Síndrome de la Pubertad". Es conocido por su personalidad apática pero de buen corazón.'},
        {'Anime': 'Bunny Girl Senpai', 'Personaje': 'Rio Futaba', 'biografia': 'Una chica de ciencias y única miembro del club de ciencias, amiga de Sakuta. Sufre un Síndrome de la Pubertad que la divide en dos versiones de sí misma.'},
        {'Anime': 'Bunny Girl Senpai', 'Personaje': 'Nodoka Toyohama', 'biografia': 'La media hermana de Mai Sakurajima y miembro de un grupo de idols. Sufre del Síndrome de la Pubertad, intercambiando cuerpos con Mai debido a su complejo de inferioridad.'},
        {'Anime': 'Bunny Girl Senpai', 'Personaje': 'Kaede Azusagawa', 'biografia': 'La hermana menor de Sakuta, que sufre de amnesia disociativa y ansiedad social debido al acoso en línea. Su objetivo es superar sus miedos y volver a salir de casa.'},
        {'Anime': 'Kaguya-sama', 'Personaje': 'Kaguya Shinomiya', 'biografia': 'Vicepresidenta del consejo estudiantil y heredera de una familia multimillonaria. Está enamorada del presidente, Miyuki Shirogane, pero su orgullo le impide confesarse.'},
        {'Anime': 'Kaguya-sama', 'Personaje': 'Chika Fujiwara', 'biografia': 'Secretaria del consejo estudiantil, una chica alegre y excéntrica que a menudo sabotea sin querer los planes de Kaguya y Miyuki. Aporta el caos y la comedia a la serie.'},
        {'Anime': 'Kaguya-sama', 'Personaje': 'Miyuki Shirogane', 'biografia': 'Presidente del consejo estudiantil, un genio académico que ha alcanzado la cima a base de esfuerzo. Está enamorado de Kaguya, pero es demasiado orgulloso para admitirlo primero.'},
        {'Anime': 'Kaguya-sama', 'Personaje': 'Yuu Ishigami', 'biografia': 'Tesorero del consejo estudiantil, un chico pesimista y otaku que vive con miedo de Kaguya. Es el protagonista de su propio arco de superación personal.'},
        {'Anime': 'Kaguya-sama', 'Personaje': 'Ai Hayasaka', 'biografia': 'Asistente personal de Kaguya Shinomiya y compañera de clase. Lleva una doble vida, actuando como una gyaru en la escuela para ocultar su verdadera identidad y apoyar a Kaguya.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Denji', 'biografia': 'Protagonista que se fusiona con su perro demonio, Pochita, para convertirse en Chainsaw Man. Trabaja como cazador de demonios para la seguridad pública con el simple sueño de tener una vida normal.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Power', 'biografia': 'Una demonio de sangre que actúa como cazadora de demonios en el escuadrón de Makima. Es infantil, egoísta y caótica, pero desarrolla un fuerte vínculo con Denji y Aki.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Makima', 'biografia': 'Una cazadora de demonios de alto rango y líder de un escuadrón especial. Es una figura enigmática y manipuladora que controla a Denji con promesas de afecto y normalidad.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Aki Hayakawa', 'biografia': 'Un cazador de demonios que trabaja bajo las órdenes de Makima. Es serio y reservado, y busca venganza contra el Demonio Pistola, que mató a su familia.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Kishibe', 'biografia': 'Un veterano y autoproclamado "cazador de demonios más fuerte". Es el capitán de la División Especial de Tokio y actúa como mentor de Denji y Power.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Yoru', 'biografia': 'Conocido como el Demonio de la Guerra, es uno de los Cuatro Jinetes que ha tomado posesión del cuerpo de Asa Mitaka. Su objetivo es hacer que la humanidad vuelva a temer a la guerra.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Asa Mitaka', 'biografia': 'Una estudiante de secundaria solitaria que se convierte en el recipiente del Demonio de la Guerra, Yoru. Lucha por mantener su identidad mientras comparte su cuerpo con el demonio.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Himeno', 'biografia': 'Una cazadora de demonios compañera de Aki Hayakawa. Tiene un contrato con el Demonio Fantasma, lo que le permite usar uno de sus brazos invisibles a costa de uno de sus ojos.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Reze', 'biografia': 'Conocida como Lady Reze o el Demonio Bomba, es una híbrida de la Unión Soviética enviada para capturar a Chainsaw Man. Desarrolla una conexión complicada con Denji.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Kobeni Higashiyama', 'biografia': 'Una ex cazadora de demonios extremadamente cobarde y ansiosa que solo trabaja por dinero para mantener a su familia. A pesar de su miedo, demuestra una agilidad sobrehumana en situaciones de vida o muerte.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Pochita', 'biografia': 'El Demonio Motosierra original y el corazón de Denji. Es el héroe del infierno, temido por los demonios, que se sacrifica para salvar a Denji y cumplir su sueño de tener una vida normal.'},
        {'Anime': 'Chainsaw Man', 'Personaje': 'Quanxi', 'biografia': 'Una híbrida y cazadora de demonios de China, considerada la "primera cazadora de demonios". Es una experta en combate cuerpo a cuerpo y maneja múltiples espadas.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Senku Ishigami', 'biografia': 'Protagonista principal, un genio científico que despierta en un mundo petrificado miles de años en el futuro. Su objetivo es reconstruir la civilización desde cero usando la ciencia.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Kohaku', 'biografia': 'Una joven descendiente de los humanos que no fueron petrificados, conocida por su increíble fuerza y agilidad. Es una de las guerreras más fuertes de la Aldea Ishigami y la primera aliada de Senku.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Chrome', 'biografia': 'El autoproclamado "científico" de la Aldea Ishigami. Se convierte en el aprendiz de Senku, mostrando una gran curiosidad y talento para la ciencia a pesar de su conocimiento primitivo.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Taiju Ooki', 'biografia': 'El mejor amigo de Senku, conocido por su resistencia física ilimitada y su gran corazón. Actúa como la fuerza bruta del Reino de la Ciencia.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Suika', 'biografia': 'Una niña pequeña de la Aldea Ishigami que usa una máscara de sandía para corregir su visión borrosa. Es una excelente exploradora y ayuda al Reino de la Ciencia con su agilidad.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Gen Asagiri', 'biografia': 'Un mentalista del viejo mundo, revivido por Tsukasa para espiar a Senku. Es un maestro del engaño y la manipulación psicológica, pero se une al Reino de la Ciencia.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Yuzuriha Ogawa', 'biografia': 'Amiga de la infancia de Senku y Taiju, y el interés amoroso de este último. Es una experta en artesanía y se encarga de reconstruir las estatuas humanas rotas.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Tsukasa Shishiou', 'biografia': 'Antagonista principal, conocido como "el estudiante de secundaria más fuerte". Busca crear un nuevo mundo sin adultos ni tecnología, lo que lo enfrenta directamente con Senku.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Ginro', 'biografia': 'Un guardia de la Aldea Ishigami, hermano de Kinro. Es cobarde y perezoso, pero puede mostrar valentía cuando es necesario para proteger a sus amigos.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Kinro', 'biografia': 'Un guardia de la Aldea Ishigami, hermano de Ginro. Es extremadamente serio y sigue las reglas al pie de la letra, pero sufre de una visión deficiente.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Kaseki', 'biografia': 'Un anciano artesano de la Aldea Ishigami con una pasión increíble por la construcción y la invención. Se convierte en el principal ingeniero del Reino de la Ciencia.'},
        {'Anime': 'Dr. Stone', 'Personaje': 'Ruri', 'biografia': 'La sacerdotisa de la Aldea Ishigami y hermana mayor de Kohaku. Padece una enfermedad debilitante hasta que Senku logra crear un antibiótico para curarla.'},
        {'Anime': 'Darling in the Franxx', 'Personaje': 'Hiro', 'biografia': 'El protagonista, un joven piloto que no puede sincronizarse con ningún compañero hasta que conoce a Zero Two. Es conocido como el "parásito problemático".'},
        {'Anime': 'Darling in the Franxx', 'Personaje': 'Goro', 'biografia': 'El mejor amigo de Hiro y un piloto excepcional y líder natural. Es maduro y responsable, y está enamorado de su compañera, Ichigo.'},
        {'Anime': 'Darling in the Franxx', 'Personaje': 'Zero Two', 'biografia': 'Una misteriosa y poderosa piloto con sangre de klaxosaurio, conocida como la "asesina de compañeros". Busca a su "darling" original y forma una pareja legendaria con Hiro.'},
        {'Anime': 'Darling in the Franxx', 'Personaje': 'Ichigo', 'biografia': 'Amiga de la infancia de Hiro y líder del Escuadrón 13. Siente un amor no correspondido por Hiro y a menudo choca con Zero Two por su afecto.'},
        {'Anime': 'Darling in the Franxx', 'Personaje': 'Zorome', 'biografia': 'Un piloto ruidoso y arrogante del Escuadrón 13 que anhela el reconocimiento de los adultos. A pesar de su actitud, se preocupa profundamente por sus compañeros.'},
        {'Anime': 'Horimiya', 'Personaje': 'Kyoko Hori', 'biografia': 'Una estudiante popular y brillante que oculta su lado hogareño. Desarrolla una relación con Izumi Miyamura después de que él descubre su secreto.'},
        {'Anime': 'Horimiya', 'Personaje': 'Yuki Yoshikawa', 'biografia': 'La mejor amiga de Kyoko Hori. Es una chica alegre y despreocupada que a menudo ayuda a sus amigos con sus problemas amorosos.'},
        {'Anime': 'Horimiya', 'Personaje': 'Izumi Miyamura', 'biografia': 'Un estudiante que parece sombrío y otaku en la escuela, pero que fuera de ella es un chico amable con tatuajes y piercings. Se enamora de Kyoko Hori.'},
        {'Anime': 'Horimiya', 'Personaje': 'Remi Ayasaki', 'biografia': 'Miembro del consejo estudiantil y novia de Kakeru Sengoku. Es una chica pequeña, linda y enérgica que parece una mascota para sus amigos.'},
        {'Anime': 'Horimiya', 'Personaje': 'Shu Iura', 'biografia': 'Un compañero de clase enérgico y caótico de Hori y Miyamura. Es el hermano mayor de Motoko Iura.'},
        {'Anime': 'Horimiya', 'Personaje': 'Tooru Ishikawa', 'biografia': 'El mejor amigo de Izumi Miyamura. Inicialmente estaba enamorado de Kyoko Hori, pero acepta su relación y se convierte en un amigo cercano de la pareja.'},
        {'Anime': 'Horimiya', 'Personaje': 'Shouta Hori', 'biografia': 'El hermano menor de Kyoko Hori. Es un niño pequeño que se encariña rápidamente con Miyamura, ayudando a fortalecer el vínculo entre él y su hermana.'},
        {'Anime': 'Viland Saga', 'Personaje': 'Thorfinn', 'biografia': 'Protagonista que comienza como un niño alegre, pero se consume por la venganza contra Askeladd tras la muerte de su padre. Su viaje lo lleva de ser un guerrero a buscar una tierra sin guerra.'},
        {'Anime': 'Viland Saga', 'Personaje': 'Askeladd', 'biografia': 'El carismático y astuto líder de una banda de mercenarios vikingos. Es el antagonista y una figura paterna compleja para Thorfinn, a quien manipula y entrena.'},
        {'Anime': 'Viland Saga', 'Personaje': 'Canute', 'biografia': 'Un príncipe danés inicialmente tímido y afeminado. Tras una tragedia personal, experimenta una profunda transformación y se convierte en un rey calculador y decidido.'},
        {'Anime': 'Viland Saga', 'Personaje': 'Bjorn', 'biografia': 'El segundo al mando de Askeladd, un berserker que lucha con una ferocidad increíble después de comer un hongo especial. Es extremadamente leal a Askeladd.'},
        {'Anime': 'Viland Saga', 'Personaje': 'Thors Snorresson', 'biografia': 'El padre de Thorfinn y un legendario guerrero conocido como el "Trol de Jom". Desertó de la guerra para vivir una vida pacífica con su familia.'},
        {'Anime': 'Viland Saga', 'Personaje': 'Thorkell', 'biografia': 'Un guerrero vikingo gigante y tío abuelo de Thorfinn que vive por y para el combate. Disfruta de la batalla más que nada y busca constantemente oponentes fuertes.'},
        {'Anime': 'Kono Subarashii', 'Personaje': 'Kazuma Satou', 'biografia': 'Un hikikomori reencarnado en un mundo de fantasía. Es el protagonista cínico y pragmático que lidera un grupo de aventureras poderosas pero disfuncionales.'},
        {'Anime': 'Kono Subarashii', 'Personaje': 'Darkness', 'biografia': 'Una paladín masoquista que anhela ser atacada por monstruos y maltratada por sus compañeros. A pesar de sus extraños deseos, tiene una defensa increíblemente alta.'},
        {'Anime': 'Kono Subarashii', 'Personaje': 'Aqua', 'biografia': 'Una diosa inútil que fue arrastrada al mundo de fantasía por Kazuma. Es poderosa contra los no muertos, pero su baja inteligencia y mala suerte la convierten en una carga.'},
        {'Anime': 'Kono Subarashii', 'Personaje': 'Megumin', 'biografia': 'Una archimaga del clan de los Demonios Carmesí, obsesionada con la magia de explosión. Solo puede lanzar un hechizo por día, que la deja completamente inmovilizada.'},
        {'Anime': 'Kono Subarashii', 'Personaje': 'Wiz', 'biografia': 'Una poderosa lich y antigua general del Rey Demonio que ahora dirige una tienda de objetos mágicos. Es amable y dulce, pero una terrible mujer de negocios.'},
        {'Anime': 'Kono Subarashii', 'Personaje': 'Luna', 'biografia': 'La recepcionista del gremio de aventureros de la ciudad de Axel. Es una mujer amable y servicial que a menudo lidia con las travesuras del grupo de Kazuma.'},
        {'Anime': 'Shin Seiki Evangelion', 'Personaje': 'Shinji Ikari', 'biografia': 'El protagonista y piloto designado de la Unidad Evangelion 01. Es un joven introvertido y depresivo que lucha con sus problemas de abandono y la presión de salvar a la humanidad.'},
        {'Anime': 'Shin Seiki Evangelion', 'Personaje': 'Misato Katsuragi', 'biografia': 'La directora de operaciones de NERV y la guardiana de Shinji y Asuka. Es una líder capaz en el trabajo, pero lleva un estilo de vida desordenado en casa.'},
        {'Anime': 'Shin Seiki Evangelion', 'Personaje': 'Rei Ayanami', 'biografia': 'La enigmática piloto de la Unidad Evangelion 00. Es extremadamente introvertida y muestra poca emoción, manteniendo una lealtad inquebrantable hacia Gendo Ikari.'},
        {'Anime': 'Shin Seiki Evangelion', 'Personaje': 'Kensuke Aida', 'biografia': 'Compañero de clase de Shinji y un entusiasta militar. Es un otaku de las armas y sueña con convertirse en piloto de Evangelion, a menudo jugando a juegos de guerra solo.'},
        {'Anime': 'Shin Seiki Evangelion', 'Personaje': 'Asuka Langley Soryu', 'biografia': 'La piloto de la Unidad Evangelion 02, una joven prodigio de Alemania. Es extremadamente orgullosa, competitiva y busca constantemente la validación de los demás.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Shinra Kusakabe', 'biografia': 'Un bombero de tercera generación con la habilidad de generar fuego desde sus pies, apodado "Huellas del Diablo". Se une a la Octava Compañía para descubrir la verdad detrás del incendio que mató a su familia.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Akitaru Obi', 'biografia': 'El capitán de la Octava Compañía, un bombero no pyrokinético que compensa su falta de poderes con una fuerza física increíble y un fuerte liderazgo. Es un modelo a seguir para su equipo.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Arthur Boyle', 'biografia': 'Un bombero de la Octava Compañía que se ve a sí mismo como un "Rey Caballero". Su poder pyrokinético le permite controlar el plasma de su espada, Excalibur, y es más fuerte cuanto más se sumerge en su delirio.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Maki Oze', 'biografia': 'Una ex militar y bombero de primera clase en la Octava Compañía. Es una experta en combate cuerpo a cuerpo y puede controlar las llamas a distancia, aunque odia que la llamen "ogro" o "gorila".'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Iris', 'biografia': 'Una monja que forma parte de la Octava Compañía. Es la encargada de rezar por las almas de los "Infernales" para que puedan descansar en paz y no tiene habilidades de combate.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Tamaki Kotatsu', 'biografia': 'Una bombero de la Primera Compañía que más tarde se une a la Octava. Es conocida por su "Sujetador de la Suerte", que la deja en situaciones comprometedoras, y su habilidad para generar llamas con forma de gato.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Leonard Burns', 'biografia': 'El capitán de la Primera Compañía, un poderoso bombero de tercera generación con un parche en el ojo. Es un veterano que conoce muchos secretos sobre la combustión humana.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Benimaru Shinmon', 'biografia': 'El capitán de la Séptima Compañía en Asakusa, conocido como el "Rey de la Destrucción". Es un híbrido de segunda y tercera generación, considerado el bombero más fuerte de todo el imperio.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Konro Sagamiya', 'biografia': 'El teniente de la Séptima Compañía y mano derecha de Benimaru. Sufrió una lesión grave llamada "Tephrosis" por usar su poder más allá de sus límites.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Joker', 'biografia': 'Un anti-héroe y criminal buscado que busca la verdad sobre el Gran Cataclismo. Es un poderoso pyrokinético que a menudo ayuda a Shinra desde las sombras.'},
        {'Anime': 'Enen no Shouboutai', 'Personaje': 'Sho Kusakabe', 'biografia': 'El hermano menor de Shinra y el comandante de los Caballeros de la Llama Cenicienta. Posee la habilidad de detener el tiempo gracias a la Gracia del Adolla.'}
    ]
    return pd.DataFrame(datos_verificados)


#Esta es la funcion con la que vamos a crear la base de datos y poblarla con los datos que tenemos
def crear_y_poblar_database():
    print("--- INICIANDO PROCESO DE CREACIÓN DE BASE DE DATOS ---")
    df_personajes = cargar_datos_verificados() #Aqui empezamos a cargar los 100 personajes
    documentos = df_personajes['biografia'].tolist() #Estamos manejando aqui solo biografias, Ya con esto lo vamos a convertir en vectores
    ids = [str(i) for i in range(len(documentos))] #Le asignamos un id a cada personaje, que es el indice de la lista de biografias como una base de datos cualquiera
    
    print("➡️ Cargando modelo de embeddings (esto puede tardar)...")
    modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')  # Carga el modelo pre-entrenado
    
    print("➡️ Generando embeddings para los 100 documentos...")
    embeddings = modelo.encode(documentos, show_progress_bar=True)# Convierte las 100 biografías en 100 vectores numéricos
    
    cliente = chromadb.PersistentClient(path="chroma_db") #Se conecta a ChromaDB y le dice que guarde todo en la carpeta de ese mismo nombre
    
    print("➡️ Creando colección para Similaridad Coseno...")
    coleccion_coseno = cliente.get_or_create_collection(name="personajes_anime_coseno", metadata={"hnsw:space": "cosine"}) # Se crean los "cajones/coleciones" dentro ya de la base de datos
    coleccion_coseno.add(embeddings=embeddings, documents=documentos, ids=ids) #Se aplican unas formulas matematicas para medir la "cercania" que es la similitud entre los vectores
    
    ### CORREGIDO: Faltaba la línea para crear la colección L2 antes de añadirle datos ###
    print("➡️ Creando colección para Distancia Euclidiana (L2)...")
    coleccion_l2 = cliente.get_or_create_collection(name="personajes_anime_l2", metadata={"hnsw:space": "l2"})
    coleccion_l2.add(embeddings=embeddings, documents=documentos, ids=ids)
    
    print("Base de datos creada y guardada en la carpeta 'chroma_db'.") #Guarda los vectores, junto con su texto original y su ID, en ambas colecciones
    print("--- PROCESO DE CREACIÓN FINALIZADO ---")

def buscar_personajes(query_text, tipo_metrica):
    df_personajes = cargar_datos_verificados()
    modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

    if not os.path.exists("chroma_db"):
        crear_y_poblar_database()

    cliente = chromadb.PersistentClient(path="chroma_db")
    
    if tipo_metrica == 'l2':
        coleccion_activa = cliente.get_collection(name="personajes_anime_l2")
    else:
        coleccion_activa = cliente.get_collection(name="personajes_anime_coseno")

    query_embedding = modelo.encode([query_text])
    
    resultados = coleccion_activa.query(query_embeddings=query_embedding, n_results=3)
    
    personajes_encontrados = []
    for i, id_str in enumerate(resultados['ids'][0]):
        idx = int(id_str)
        distancia = resultados['distances'][0][i]
        personaje = df_personajes.iloc[idx]
        personajes_encontrados.append({
            'Personaje': personaje['Personaje'],
            'Anime': personaje['Anime'],
            'distancia': f"{distancia:.4f}"
        })
        
    return personajes_encontrados

if __name__ == "__main__":
    if not os.path.exists("chroma_db"):
        crear_y_poblar_database()