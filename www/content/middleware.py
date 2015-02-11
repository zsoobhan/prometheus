from . import service


class QuestionMiddleware(object):

    def process_request(self, request):
        if not request.session.get('q_and_a'):
            question = "What is %s + %s?" % service.generate_words()
            answer = service.generate_answer(question)

            request.session['q_and_a'] = {'question': question,
                                          'answer': answer, }
