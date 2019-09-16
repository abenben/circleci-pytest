# -*- coding: utf-8 -*-


class Calculator(object):
    """
    四則演算を行う。
    """

    @staticmethod
    def addition(x, y):
        """
        加算を行う。
        :param x: 左辺
        :param y: 右辺
        :return: 計算結果
        """
        result = x + y
        return result

    @staticmethod
    def subtraction(x, y):
        """
        減算を行う。
        :param x: 左辺
        :param y: 右辺
        :return: 計算結果
        """
        result = x - y
        return result

    @staticmethod
    def multiplication(x, y):
        """
        乗算を行う。
        :param x: 左辺
        :param y: 右辺
        :return: 計算結果
        """
        result = x * y
        return result

    @staticmethod
    def division(x, y):
        """
        割算を行う。
        :param x: 左辺
        :param y: 右辺
        :return: 計算結果
        """
        result = x / y
        return result
