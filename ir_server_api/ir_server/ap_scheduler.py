import glob
from datetime import datetime

import ir_server.moisture_map as moisture_map
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.files.images import ImageFile
from models import Stat


def periodic_execution():
    asc_list = sorted(glob.glob("data/*.png"))[-10:-1]
    heat_np_list = [moisture_map.read_from_png(f) for f in asc_list]
    heat_map = np.stack(heat_np_list, axis=2)

    x0, x1, y0, y1 = 318, 361, 318 + 10, 361 + 10  # 参照物体の領域
    ref_heat = np.array([np.average(h[x0:x1, y0:y1]) for h in heat_np_list.copy()])

    cov_map = moisture_map.calc_cov_map(heat_map, ref_heat)

    sns.heatmap(cov_map, cmap="bwr_r", robust=True)  # bwr_r
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    current_time = datetime.now().strftime("%Y-%m-%d-%H%M%S%f")
    file_name = f"data/{current_time}.png"
    plt.savefig(file_name, format="png", bbox_inches="tight", pad_inches=0.05, dpi=600)
    stat = Stat.objects.create(name=file_name)
    stat.file = ImageFile(open(file_name, "rb"))
    stat.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution, "interval", minute=1)  # 毎日23時59分に実行
    scheduler.start()
