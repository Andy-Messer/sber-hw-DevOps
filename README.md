# sber-hw-DevOps
## Установите docker и minikube

 - https://docs.docker.com/get-docker/
 - https://minikube.sigs.k8s.io/docs/start/

### Доступные адреса

 - `localhost:8000/time`
 - `localhost:8000/statistics`

## Testing hw commands
> Предположим docker и minikube у Вас уже запущены.

> Создайте директорию, куда будут сохраняться логи и примонтируйтесь к ней
```bash
mkdir {your_dir}
minikube mount {your_dir}:/data
```

## Example
```bash
mkdir data
minikube mount data:/data
```

> Откройте новый терминал и запустите pod с манифестом `deployment-web.yaml`

```bash
kubectl apply -f deployment-web.yaml
```

> Прокиньте порты
```bash
kubectl port-forward my-pod 8000:8000
```

> Далее в директории, выбранной ранее будет появляться искомый файл `logstats.txt`. Со статистикой обращений к адресу `localhost:8000/time`


