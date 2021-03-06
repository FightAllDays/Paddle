# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import logger
from . import progressbar
from . import callbacks
from . import download

from . import model
from .model import *

from . import metrics
from . import datasets
from . import distributed
from . import vision
from . import text

from . import device
from .device import *

from .dygraph_layer_patch import monkey_patch_layer

logger.setup_logger()

__all__ = [
    'callbacks',
    'datasets',
    'distributed',
    'download',
    'metrics',
    'vision',
    'text',
] + model.__all__ + device.__all__

monkey_patch_layer()
