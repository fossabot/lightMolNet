# -*- coding: utf-8 -*-
# ====================================== #
# @Author  : Yanbo Han
# @Email   : yanbohan98@gmail.com
# @File    : __init__.py.py
# ALL RIGHTS ARE RESERVED UNLESS STATED.
# ====================================== #

import os

from lightMolNet.data.atoms import AtomsData, get_center_of_mass, logger
from lightMolNet.environment import SimpleEnvironmentProvider


class FileSystemAtomsData(AtomsData):
    r"""
    Base class for local file system data.
    Notice to Implement the method `_proceed`.

    Parameters
    ----------
    dbpath:str

    filecontextdir:str or dict
        specific format depend on child class

    """

    def __init__(
            self,
            dbpath: str,
            filecontextdir: str or dict,
            subset=None,
            load_only=None,
            available_properties=None,
            units=None,
            environment_provider=SimpleEnvironmentProvider(),
            collect_triples=False,
            centering_function=get_center_of_mass,
            proceed=False,
    ):
        self.filecontextdir = filecontextdir
        super().__init__(dbpath=dbpath,
                         subset=subset,
                         available_properties=available_properties,
                         load_only=load_only,
                         units=units,
                         environment_provider=environment_provider,
                         collect_triples=collect_triples,
                         centering_function=centering_function, )
        if proceed:
            self.proceed()

    def proceed(self):
        """
        Wrapper function for proceed files.
        """
        if os.path.exists(self.dbpath):
            logger.info(
                "The database has already been proceed and stored "
                "at {}. Check your data.".format(self.dbpath)
            )
        elif not os.path.exists(self.filecontextdir):
            logger.error(
                "The files directory does not exist! Check if "
                "{} is your data directory.".format(os.path.abspath(self.filecontextdir))
            )
        else:
            self._proceed()

    def _proceed(self):
        raise NotImplementedError
