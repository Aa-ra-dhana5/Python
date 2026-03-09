import asyncio
import time

async def func1():
    print("hello")
    time.sleep(4)
async def func2():
    print("func2")
    time.sleep(4)

async def func3():
    print("func 3")
    time.sleep(4)

    
    
async def main():
    start =time.time()
    await func1()
    await func2()
    await func3()
    
    result = time.time()- start
    print(result , "this is time taken without async")
   
   # gather() helps to run all the function parallaly 
# async def main():
#    start = time.time()
#    L=  await asyncio.gather(
#         func1(),
#         func2(),
#         func3()
#     )
   
#    result = time.time()- start
#    print(result , "this is time taken while async")
    

asyncio.run(main())