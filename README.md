1. Склонировать проект git clone https://github.com/CROWIER/incident_manager.git
2. cp .env.example .env
3. отредактировать env файл
4. собрвть и запустить образ docker-compose up --build
5. api доступен по http://localhost:8000/docs

Примеры запросов:
# Создать инцидент
curl -X POST http://localhost:8000/incidents/ \
  -H "Content-Type: application/json" \
  -d '{"description": "Самокат сломался", "source": "operator"}'

# Получить все инциденты
curl http://localhost:8000/incidents/

# Фильтр по статусу
curl http://localhost:8000/incidents/\?status=new

# Обновить статус
curl -X PATCH http://localhost:8000/incidents/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "in_progress"}'