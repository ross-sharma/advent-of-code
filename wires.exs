# https://adventofcode.com/2024/day/24

defmodule Swapper do
  def main(filename) do
    wires_map = Wires.get_wires_map(filename)
    unbound_keys = Wires.get_unbound_keys(wires_map)
    try_swaps(wires_map, unbound_keys)
  end

	defp set_wire(map, key, val) do
    Map.put(map, key, {:bound, val})
	end

  defp run_test(map) do
    map = set_wire(map, "x00", "1")
    map = set_wire(map, "x01", "1")
    map = set_wire(map, "x02", "1")
    map = set_wire(map, "x03", "0")

    map = set_wire(map, "y00", "1")
    map = set_wire(map, "y01", "0")
    map = set_wire(map, "y02", "0")
    map = set_wire(map, "y03", "0")

    exp = "0001"

    # IO.puts("Running test")
    # IO.inspect(map)
    res = Wires.resolve_all(map)

    if res == :cycle do
      IO.puts("Result cycle")
      false
    else
      {bin, _} = Wires.eval_wires(res, "z")
      #IO.puts("Result #{bin}")
      bin == exp
    end
  end

  defp try_swaps(wires_map, unbound_keys) do
    try_swaps(wires_map, unbound_keys, {0, 0, 0, 0})
  end

  defp try_swaps(_wires_map, _unbound_keys, nil) do
    IO.puts("Ran out of swaps to try")
    nil
  end

  defp try_swaps(wires_map, unbound_keys, swap_indices) do
		{a,b,c,d} = swap_indices

    swap_keys = {
      Enum.at(unbound_keys, a),
      Enum.at(unbound_keys, b),
      Enum.at(unbound_keys, c),
      Enum.at(unbound_keys, d)
    }

    new_map = get_swapped_wires(wires_map, swap_keys)

    if run_test(new_map) do
      IO.puts("Test passed")
      IO.inspect(new_map)
      IO.inspect(swap_indices)
      IO.inspect(swap_keys)
    else
      new_swaps = next_swap(swap_indices, length(unbound_keys) - 1)
			IO.inspect(new_swaps)
      try_swaps(wires_map, unbound_keys, new_swaps)
    end
  end

  defp get_swapped_wires(wires_map, {key1, key2, key3, key4}) do
    tmp = wires_map[key1]
    wires_map = Map.put(wires_map, key1, wires_map[key2])
    wires_map = Map.put(wires_map, key2, tmp)

    tmp = wires_map[key3]
    wires_map = Map.put(wires_map, key3, wires_map[key4])
    wires_map = Map.put(wires_map, key4, tmp)

    wires_map
  end

  defp next_swap({a, b, c, d}, max_index) do
    if d < max_index do
      {a, b, c, d + 1}
    else
      if c < max_index-1 do
        {a, b, c + 1, c + 2}
      else
        if b < max_index-2 do
          {a, b + 1, a + 1, a + 2}
        else
          if a < max_index-3 do
            {a + 1, a + 2, a + 3, a + 4}
          else
            nil
          end
        end
      end
    end
  end

  # module
end

defmodule Wires do
  def main(filename) do
    wires_map = get_wires_map(filename)
    result = resolve_all(wires_map)

    if result == :cycle do
      IO.puts("Cycle detected")
      System.halt(1)
    end

    {bin, dec} = eval_wires(result, "z")
    IO.inspect(bin)
    IO.inspect(dec)
  end

  def get_wires_map(filename) do
    lines = get_lines(filename)
    wires_list = Enum.map(lines, fn l -> parse_line(l) end)
    map_wires(wires_list, %{})
  end

  def eval_wires(wires_map, prefix) do
    z_keys =
      Enum.filter(
        Map.keys(wires_map),
        fn key -> String.starts_with?(key, prefix) end
      )

    z_keys = Enum.sort(z_keys)

    bin_str = get_bin_str(z_keys, wires_map, "")
    bin = String.reverse(bin_str)
    dec = bin_str_to_num(bin_str)
    {bin, dec}
  end

  def bin_str_to_num(bin_str) do
    bin_str_to_num(bin_str, 0, 0)
  end

  def bin_str_to_num(bin_str, current_num, index) do
    if index >= String.length(bin_str) do
      current_num
    else
      char = String.at(bin_str, index)

      new_num =
        if char == "1" do
          current_num + 2 ** index
        else
          current_num
        end

      bin_str_to_num(bin_str, new_num, index + 1)
    end
  end

  def get_bin_str(keys, map, current_str) do
    if keys == [] do
      current_str
    else
      key = hd(keys)
      {:bound, val} = map[key]
      get_bin_str(tl(keys), map, current_str <> val)
    end
  end

  def print_map(wires_map) do
    Enum.each(
      wires_map,
      fn {key, val} ->
        boundval = elem(val, 1)
        IO.puts("#{key}: #{boundval} ")
      end
    )
  end

  def get_unbound_keys(wires_map) do
    Enum.filter(
      Map.keys(wires_map),
      fn key -> elem(wires_map[key], 0) == :unbound end
    )
  end

  def resolve_all(wires_map) do
    unbound_keys = get_unbound_keys(wires_map)

    if unbound_keys == [] do
      wires_map
    else
      key = hd(unbound_keys)

      case resolve(key, wires_map) do
        :cycle -> :cycle
        {new_wires, _} -> resolve_all(new_wires)
      end
    end
  end

  defp resolve(key, wires_map) do
    resolve(key, wires_map, %{})
  end

  defp resolve(key, wires_map, visited) do
    if Map.has_key?(visited, key) do
      :cycle
    else
      new_visited = Map.put(visited, key, nil)

      case wires_map[key] do
        {:bound, val} ->
          {wires_map, val}

        {:unbound, key1, key2, gate} ->
          case resolve(key1, wires_map, new_visited) do
            :cycle ->
              :cycle

            {new_map, val1} ->
              case resolve(key2, new_map, new_visited) do
                :cycle ->
                  :cycle

                {new_map, val2} ->
                  new_val = apply_gate(gate, val1, val2)
                  new_map = Map.put(new_map, key, {:bound, new_val})
                  {new_map, new_val}
              end
          end
      end
    end
  end

  defp apply_gate(gate, val1, val2) do
    result =
      case gate do
        "AND" -> val1 == "1" and val2 == "1"
        "OR" -> val1 == "1" or val2 == "1"
        "XOR" -> val1 != val2
      end

    if result do
      "1"
    else
      "0"
    end
  end

  defp map_wires(wires_list, current_map) do
    case wires_list do
      [] ->
        current_map

      _ ->
        wire = hd(wires_list)

        new_map =
          case wire do
            {:bound, key, val} ->
              Map.put(current_map, key, {:bound, val})

            {:unbound, key, in_key1, in_key2, gate} ->
              Map.put(current_map, key, {:unbound, in_key1, in_key2, gate})
          end

        map_wires(tl(wires_list), new_map)
    end
  end

  defp parse_line(line) do
    if String.contains?(line, ":") do
      [key, val] = String.split(line, ": ")
      {:bound, key, val}
    else
      [left_side, key] = String.split(line, " -> ")
      [in1, gate, in2] = String.split(left_side, " ")
      {:unbound, key, in1, in2, gate}
    end
  end

  defp get_lines(filename) do
    case File.read(filename) do
      {:ok, body} ->
        all_lines = String.split(body, "\n")
        Enum.filter(all_lines, fn x -> String.length(x) > 0 end)

      {:error, reason} ->
        IO.puts("Could not open the file #{filename}: #{reason}")
        System.halt(1)
    end
  end
end

filename = hd(System.argv())
# Wires.main(filename)
Swapper.main(filename)
