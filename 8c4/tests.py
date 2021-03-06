import game_simulator 
import hand_evaluation

def compare_hands(handA, handB):
  handA = [game_simulator.string_to_card(x) for x in handA]
  handB = [game_simulator.string_to_card(x) for x in handB]
  return hand_evaluation.poker_hand_comparator(handA, handB)

def assert_correct(hand_1, hand_2, value):
  actual_value = compare_hands(hand_1, hand_2)
  try:
    assert actual_value == value
  except:
    print 'Test failed!'
    print '  Hand 1: ', hand_1
    print '    classification: ', hand_evaluation.classify_hand([game_simulator.string_to_card(x) for x in hand_1])
    print '  Hand 2: ', hand_2
    print '    classification: ', hand_evaluation.classify_hand([game_simulator.string_to_card(x) for x in hand_2])
    print '  Should have been: ' , value
    print '  Instead was     : ' , actual_value
    print

def test_hands_list(hands_list):
  for i in range(len(hands_list)):
    for j in range(i+1, len(hands_list)):
      # print hands_list[i]
      # print hands_list[j]
      # print
      assert_correct(hands_list[i], hands_list[j], 1)
      assert_correct(hands_list[j], hands_list[i], -1)

hands_list = [
  ['10c',  'Jc',  'Qc',  'Kc',  'Ac'], # straight flush
  [ '2c',  '3c',  '4c',  '5c',  '6c'], # straight flush
  [ 'Ac',  '2c',  '3c',  '4c',  '5c'], # straight flush
  [ '2c',  '2d',  '2h',  '2s',  '6c'], # 4 of a kind
  [ '2c',  '2d',  '2h',  '6s',  '6c'], # full house
  [ '2c',  '3c',  '4c',  '5c',  '7c'], # flush
  ['10c',  'Jc',  'Qc',  'Kc',  'Ad'], # straight 
  [ '2c',  '3c',  '4c',  '5c',  '6d'], # straight
  [ 'Ac',  '2c',  '3c',  '4c',  '5d'], # straight
  [ '2c',  '2d',  '2h',  '5s',  '6c'], # 3 of a kind
  [ '2c',  '2d',  '4h',  '6s',  '6c'], # 2 pair
  [ '2c',  '2d',  '3c',  '4c',  '6c'], # pair
  [ '2c',  '3c',  '4c',  '5c',  '7d'], # high
]

test_hands_list(hands_list)

hands_list = [
  ['2c', '2s', '5c', '6c', '6s'],
  ['2c', '2s', '4c', '6c', '6s'],
  ['2c', '2s', '3c', '6c', '6s'],
]

test_hands_list(hands_list)

# testing straights
hands_list = [
  ['10c',  'Jd',  'Qh',  'Ks' ,  'Ac'],
  [ '9c', '10d',  'Jh',  'Qs' ,  'Kc'],
  [ '8c',  '9d', '10h',  'Js' ,  'Qc'],
  [ '7c',  '8d',  '9h', '10s' ,  'Jc'],
  [ '6c',  '7d',  '8h',  '9s' , '10c'],
  [ '5c',  '6d',  '7h',  '8s' ,  '9c'],
  [ '4c',  '5d',  '6h',  '7s' ,  '8c'],
  [ '3c',  '4d',  '5h',  '6s' ,  '7c'],
  [ '2c',  '3d',  '4h',  '5s' ,  '6c'],
  [ 'Ac',  '2d',  '3h',  '4s' ,  '5c'],
]

test_hands_list(hands_list)

# two-pair
hands_list = [
  ['4c', '4s', '5c', '6c', '6s'],
  ['3c', '3s', '5c', '6c', '6s'],
  ['2c', '2s', '5c', '6c', '6s'],
  ['3c', '3s', '5c', '4c', '4s'],
  ['2c', '2s', '5c', '4c', '4s'],
  ['2c', '2s', '5c', '3c', '3s'],
  ['2c', '4s', '5c', '6c', '6s'],
  ['2c', '3s', '5c', '6c', '6s'],
]

test_hands_list(hands_list)

# pairs
hands_list = [
  ['2c', '3s', '4c', 'Ac', 'As'],
  ['2c', '4s', '5c', '6c', '6s'],
  ['2c', '3s', '5c', '6c', '6s'],
  ['2c', '3s', '4c', '6c', '6s'],
  ['Ac', '3s', '4c', '5c', '5s'],
  ['2c', '3s', '4c', '5c', '5s'],
]

test_hands_list(hands_list)

# high card
hands_list = [
  [ '7c',  '9s',  'Jc',  'Kc',  'As'],
  [ '5c',  '7s',  '9c',  'Jc',  'Ks'],
  [ '3c',  '7s',  '9c',  'Jc',  'Ks'],
  [ '2c',  '3s',  '9c',  'Jc',  'Ks'],
  [ '2c',  '7s',  '8c',  'Jc',  'Ks'],
  [ '2c',  '7s',  '9c', '10c',  'Ks'],
  [ '2c',  '3s',  '4c',  '9c',  'Js'],
  [ '5c',  '6s',  '7c',  '8c',  'Js'],
]

test_hands_list(hands_list)

handA = ['2c', '3c', '4c', '5c', '6c']
handB = ['2d', '3d', '4d', '5d', '6d']
assert_correct(handA, handB, 0)

handA = ['2c', '2d', '4c', '3c', '3d']
handB = ['2h', '2s', '4h', '3h', '3s']
assert_correct(handA, handB, 0)

handA = ['2c', '2d', '4c', '3c', '3d']
handB = ['2h', '2s', '4h', '3h', '3s']
assert_correct(handA, handB, 0)

handA = ['2c', '4d', '8c', 'Qc', 'Ad']
handB = ['2h', '4s', '8h', 'Qh', 'As']
assert_correct(handA, handB, 0)


