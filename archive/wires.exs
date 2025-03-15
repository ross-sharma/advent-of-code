# https://adventofcode.com/2024/day/24

defmodule Wires do
	def main(filename) do
		lines = get_lines(filename)
		wires_list = Enum.map(lines, fn l -> parse_line(l) end)
		wires_map = map_wires(wires_list, %{})
		wires_map = resolve_all(wires_map)
		
		z_keys = Enum.filter(
			Map.keys(wires_map),
			fn key -> String.starts_with?(key, "z") end
		)
		z_keys = Enum.sort(z_keys)
		
		bin_str = get_bin_str(z_keys, wires_map, "")
		IO.inspect(String.reverse(bin_str))
		num = bin_str_to_num(bin_str)
		IO.inspect(num)
	end

	def bin_str_to_num(bin_str) do 
		bin_str_to_num(bin_str, 0, 0)
	end

	def bin_str_to_num(bin_str, current_num, index) do
		if index >= String.length(bin_str) do
			current_num
		else
			char = String.at(bin_str, index)
			new_num = if char == "1" do
				current_num + 2**index
			else
				current_num
			end
			bin_str_to_num(bin_str, new_num, index+1)
		end
	end

	def get_bin_str(keys, map, current_str) do
		if keys == [] do
			current_str
		else
			key = hd(keys)	
			{:bound, val} = map[key]
			get_bin_str( tl(keys), map, current_str <> val )
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

	defp resolve_all(wires_map) do
		unbound_keys = Enum.filter(
			Map.keys(wires_map),
			fn key -> elem(wires_map[key], 0) == :unbound end
		)
		
		if unbound_keys == [] do
			wires_map
		else
			key = hd(unbound_keys)
			{new_wires, _} = resolve(key, wires_map)
			resolve_all(new_wires)
		end
	end

	defp resolve(key, wires_map) do
		case wires_map[key] do

			{:bound, val} -> 
				{wires_map, val}

			{:unbound, key1, key2, gate} ->
				{new_map, val1} = resolve(key1, wires_map)
				{new_map, val2} = resolve(key2, new_map)
				new_val = apply_gate(gate, val1, val2)
				{
					Map.put(new_map, key, {:bound, new_val}),
					new_val,
				}
		end
	end

	defp apply_gate(gate, val1, val2) do
		result = case gate do
			"AND" -> val1 == "1" and val2 == "1"
			"OR" -> val1 == "1" or val2 == "1"
			"XOR" -> val1 != val2
		end
		if result do "1" else "0" end
	end

	defp map_wires(wires_list, current_map) do
		case wires_list do
			[] -> 
				current_map
			_ -> 
				wire = hd(wires_list)
				new_map = case wire do
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
			{ :bound, key, val, }
		else
			[left_side, key] = String.split(line, " -> ")
			[in1, gate, in2] = String.split(left_side, " ")
			{ :unbound, key, in1, in2, gate, }
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

filename = hd(System.argv)
Wires.main(filename)

