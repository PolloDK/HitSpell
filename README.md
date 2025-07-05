# Hitanalyzer
Proyecto de análisis de pistas musicales en base a sus características de audio. Proyecto Final Bootcamp Le Wagon Data Science &amp; AI

https://kitt.lewagon.com/camps/1959/challenges?path=07-ML-Ops%2F03-Automate-model-lifecycle%2FRecap

https://kitt.lewagon.com/knowledge/cheatsheets/mlflow_hosting

##Pushing Image
gcloud artifacts repositories create hitalyzer-pred --repository-format=docker \
--location=europe-west1 --description="Repository for storing Hitalyzer predict image"

docker build \
  --platform linux/amd64 \
  -t $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/taxifare/$GAR_IMAGE:prod .

docker tag predict:v2.4 europe-west1-docker.pkg.dev/lewagondata1959/hitalyzer-pred/hitalyzer:prod

gcloud run deploy --image $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/taxifare/$GAR_IMAGE:prod --memory $GAR_MEMORY --region $GCP_REGION --env-vars-file .env.yaml
docker run  -p 8585:8585 -e PORT=8585 predict:v2.4   

gcloud run deploy hitanalyzer-api \
  --image europe-west1-docker.pkg.dev/lewagondata1959/hitalyzer-pred/hitalyzer:prod \
  --platform managed \
  --memory 2Gi
  --region europe-west1 \
  --set-env-vars MODEL_TARGET=local,PORT=8000