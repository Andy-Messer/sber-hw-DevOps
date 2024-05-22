#!/bin/bash

kubectl apply -f deployment-web.yaml
kubectl apply -f service.yaml
kubectl apply -f scheduled-client.yaml