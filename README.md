# cqgothic
python Library for making gothic architecture.

![](./documentation/image/cover.png)


### Example Usage

``` python
import cadquery as cq
from cqgothic import Bunker

bp = Bunker()
bp.inset=15
bp.width=140
bp.length=110
bp.height=65

bp.render_windows=True
bp.skip_windows = []
bp.window_length = 18
bp.window_height = 8
bp.window_frame_chamfer = 1.6
bp.window_frame_chamfer_select = "<Z"

bp.render_doors=True
bp.door_panels = [0, 3]

bp.render_ladders=True
bp.ladder_panels = [8]

bp.render_floor_tiles=True
bp.render_roof=False

bp.make()
rec = bp.build()

cq.exporters.export(rec,'bunker.stl')
```

## Project Documentation
* [Bunker](./documentation/bunker.md)

## Changes
* [Changelog](./changes.md)

## Dependencies
* [CadQuery 2.x](https://github.com/CadQuery/cadquery)
* [cqterrain](https://github.com/medicationforall/cqterrain)

---

## Installation
To install skirmishbunker directly from GitHub, run the following `pip` command:

	pip install git+https://github.com/medicationforall/cqgothic

**OR**

### Local Installation
From the cloned skirmishbunker directory run.

	pip install ./

---

## Running Example Scripts
[example_runner.py](example_runner.py) runs all examples.

``` bash
C:\Users\<user>\home\3d\cqgothic>python example_runner.py
```

**OR**

### Running individual examples
* From the root of the project run one of the example scripts:
  
``` bash
C:\Users\<user>\home\3d\cqgothic>python ./example/bunker.py
```