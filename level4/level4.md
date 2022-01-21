* Vyzkoušejte a napište všechny způsoby (včetně konkrétní podoby příkazu), které vás napadnou, jak:
    * spustit nginx
        * k apply -f nginx_deploy.yaml
        * k create deploy nginx --image=nginx
    * naškálovat na 3 repliky
        * upravit yaml a k apply -f ...
        * k scale deployment nginx --replicas=3
        * k edit deployment nginx
    * zobrazit všechny pody tohoto deploymentu včetně IP adresy a nodu
        k get pod -l=app=nginx -o wide
    * totéž, ale tentokrát jméno podu a image
    * switch na novější verzi
    * nastavit ENV proměnnou NGINX_INSTANCE=nginx1
    * vytvořit secret "nginx", data:
        * username: nginx
        * password: heslo
    * vypsat hodnotu z pole "password" z tohoto secretu v plain textu
    * zpřístupnit data z tohoto secretu do nginx kontejnerů
    * restartovat nginx (a zde se i zamyslete nad výhodami a navýhodami jednotlivých postupů)
* Dále si vyzkoušejte mazání zdrojů za různých okolností - opět všechny varianty, které vás napadnou
    * vytvořte deployment a service pro nginx a libovolnou configMap
        * zobrazte jedním příkazem všechny tyto zdroje
        * a smažte
    * vyzkoušejte si na deploymentu nginx:
    * mazání deploymentu kaskádově a bez kaskády - co všechno se smaže a co zůstane
    * mazání s finalizerem