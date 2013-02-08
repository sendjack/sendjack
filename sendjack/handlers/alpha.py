"""
    alpha
    -----

    A set of landing/posting pages for our alpha test.

"""
import mailer

from view.app.alpha_signup.body import SignUpBody, NewTaskBody, ThankYouBody

from post import PostHandler


class SignUpPostingHandler(PostHandler):

    _NEXT_URL = "/posting/newtask"

    def _render_body_markup(self, model=None):
        return SignUpBody()


    def _process_post_request(self):
        """Process the form data."""
        form_data = self.get_request_arguments()
        first_name = form_data.get("first-name")
        last_name = form_data.get("last-name")
        email = form_data.get("email")
        mailer.send_message(
                email,
                "jack-test@sendjack.com",
                "NEW USER: {} {}".format(first_name, last_name),
                "EMAIL: {}\nFIRST NAME: {}\nLAST NAME: {}".format(
                        email,
                        first_name,
                        last_name))


class NewTaskPostingHandler(PostHandler):

    _NEXT_URL = "/posting/thankyou"

    def _render_body_markup(self, model=None):
        return NewTaskBody()


    def _process_post_request(self):
        """Process the form data."""
        form_data = self.get_request_arguments()
        task_title = form_data.get("task-title")
        task_description = form_data.get("task-description")
        task_deadline = form_data.get("task-deadline")
        mailer.send_message(
                "jack@sendjack.com",
                "jack-test@sendjack.com",
                "NEW TASK: {}".format(task_title),
                "TASK TITLE: {}\nDESCRIPTION: {}\nDEADLINE: {}".format(
                        task_title,
                        task_description,
                        task_deadline))


class ThankYouPostingHandler(PostHandler):

    _NEXT_URL = None

    def _render_body_markup(self, model=None):
        return ThankYouBody()
