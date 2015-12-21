import tornado.ioloop
import tornado.web
from iMathModelosPredictivos.common.util.iMathServicesError import iMathServicesError
from iMathModelosPredictivos.controllers.modelBestCandidatesController import ModelBestCandidatesController


class SelectBestCandidatesHandler(tornado.web.RequestHandler):


    def get(self):

        selection_number=self.get_argument("selection_number", None, True)
        priority=self.get_argument("priority", None, True)

        modelController = ModelBestCandidatesController()
        self.write({
            "result":modelController.execute(selection_number, priority)})

