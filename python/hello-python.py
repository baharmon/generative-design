"""Hops Server"""
import ghhops_server as hs
# import rhino3dm

hops = hs.Hops()


@hops.component(
    "/hello",
    name="Hello",
    nickname="Hello",
    description="Write a hello world message with CPython",
    inputs=[
        hs.HopsString("Name", "Name", "Input Name")],
    outputs=[hs.HopsString("Message", "Message", "Hello World Message")]
)
def hello(a):
    return f"Hello {a}!"


if __name__ == "__main__":
    hops.start(debug=True)
