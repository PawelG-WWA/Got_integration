from flask.views import MethodView
from flask_smorest import Blueprint
from openai import OpenAI

contact_blueprint = Blueprint("contact", __name__)


@contact_blueprint.route("/contact")
class Contact(MethodView):
    client=OpenAI()
    
    @contact_blueprint.response(200)
    def get(self):
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system", "content":"You are a pop singer"},
                {"role":"user", "content":"compose a song about .NET garbage collector basics"}
            ]
        )
        print (completion.choices[0].message.content)
        return { 'aaa': completion.choices[0].message.content }