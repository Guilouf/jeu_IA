import random as rd


class Matrice:
    """
    Toutes les carac de l'individu sont décrites dans le dico
    reprod: la libido de l'individu: partie elevé: puberté; basse: menaupause
    """

    def __init__(self):
        self.dico_matri = {'reprod': rd.uniform(-10, 10),
                           'sexe': rd.uniform(-10, 10),
                           'age': 0}

    def reproduction(self, concub):
        """

        :param concub:
        :return:
        """
        if not isinstance(concub, self.__class__):  # vérifie que la colision ne soit pas avec une bordure
            return False
        reprod = self.dico_matri['reprod']
        sexe_concub = concub.dico_matri['reprod']
        if 7 < reprod < 10 and 2 < sexe_concub < 8:  # range marche pas pour les floats
            print("reproduction!!")
            # self.dico_matri['reprod'] = 1.0  # castre
            self.dico_matri['reprod'] += -1.0  # réduit fertilité
            return True

    def viellation(self):
        """
        Ajoute de l'age
        :return:
        """
        pass