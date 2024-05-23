#!/bin/bash

kubectl delete deployment app-deployment
kubectl delete service app-service
kubectl delete deployment statistics-client