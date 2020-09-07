# app.py

"""Main app"""

# Retic
from retic import Router, App as app

"""Define Router instance"""
router = Router()

"""Define paths"""
router \
    .get("/", lambda req, res, next: res.ok({"msg": "Hello world! - HTTP GET"})) \
    .post("/", lambda req, res, next: res.ok({"msg": "Hello world! - HTTP POST"})) \
    .put("/", lambda req, res, next: res.send({"msg": "Hello world! - HTTP PUT"})) \
    .delete("/", lambda req, res: res.send({"msg": "Hello world! - HTTP DELETE"}))

"""Import router to App"""
app.use(router)

"""Create web server"""
app.listen(
    hostname="localhost",
    port=1801
)
