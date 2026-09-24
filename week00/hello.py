import sys,time,platform
from pathlib import Path
import os

def main():

    keys=os.environ["LLM_API_KEY"]
    print("KEY:",keys)

    print("python:",sys.version.split()[0])
    print("平台：",platform.platform())

    nums=[x*x for x in range(1,11) if x%2==0]
    print("偶数平方:",nums)

    person={"name":"learner","weeks":16,"stack":["C#","python"]}
    print("姓名：",person["name"],"| 目标周数:",person["weeks"])

    p=Path("out.txt")
    p.write_text("环境跑通了\n",encoding="utf-8")
    print("写回内容:",p.read_text(encoding="utf-8").split())

    #4) 计时(后面要测API延迟)
    t0=time.time()
    time.sleep(0.3)
    print(f"耗时：{time.time()-t0:.3f}s")

if __name__=="__main__":
    main()