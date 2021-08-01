import re
def handleError(error:str)->str:
    if error.startswith("You are on cooldown. Try again in"):
        er = re.findall(r"[0-9]+", error)
        time = secTotime(int(er[0]))
        return f"You are on a cooldown. Try again in {time}"
    return error
def secTotime(inp:int)->str:
    if inp/3600>=1:
        return f"{int(inp/3600)}hr {int(inp%3600/60)} min"
    if inp/60>=0:
        return f"{int(inp/60)} min {int(inp%60)}s"
    return f"{inp}s"
if __name__=="__main__":
    r = handleError("You are on cooldown. Try again in 33362.11s")
    print(r)
