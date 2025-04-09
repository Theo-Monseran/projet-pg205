import jack
import miditoolkit.midi

client = jack.Client('Client')

inport = client.inports.register('in1')
outport = client.outports.register('out1')

client.activate()
client.connect(inport, 'systeme:capture_1')

if __name__ == '__main__':
    print(client.get_ports('*'))
    print(client.get_all_connections())
