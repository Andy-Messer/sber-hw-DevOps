#!/bin/bash

kubectl delete pod my-pod
kubectl delete service my-pod-service
kubectl delete job my-one-shot-task