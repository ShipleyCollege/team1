import sys

print("P1 -> " + sys.argv[1])
print("P2 -> " + sys.argv[2])
print("P3 -> " + sys.argv[3])

sys.path.append('../ExtractAndAnalyzeCode')
import ExtractNodes

ExtractNodes.DoItNow(sys.argv[1], sys.argv[2], sys.argv[3], debug=False)

