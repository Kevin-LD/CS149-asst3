from PIL import Image, ImageDraw
import argparse


TILE_SIZE = 16


def draw_tile_grid(input_path, output_path, tile_size=TILE_SIZE):
    img = Image.open(input_path).convert("RGB")
    width, height = img.size

    draw = ImageDraw.Draw(img)

    # Grid color: bright blue
    grid_color = (0, 0, 255)

    # Vertical lines
    for x in range(0, width, tile_size):
        draw.line([(x, 0), (x, height - 1)], fill=grid_color, width=2)

    # Horizontal lines
    for y in range(0, height, tile_size):
        draw.line([(0, y), (width - 1, y)], fill=grid_color, width=2)

    # Optional: draw the right/bottom boundary as well
    draw.line([(width - 1, 0), (width - 1, height - 1)],
              fill=grid_color, width=2)
    draw.line([(0, height - 1), (width - 1, height - 1)],
              fill=grid_color, width=2)

    img.save(output_path, format="PPM")

    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print(f"Image size: {width} x {height}")
    print(
        f"Tiles: {(width + tile_size - 1) // tile_size} x "
        f"{(height + tile_size - 1) // tile_size}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Draw a tile grid on a PPM image."
    )
    parser.add_argument("input", help="Input .ppm file")
    parser.add_argument("output", help="Output .ppm file")
    parser.add_argument(
        "--tile-size",
        type=int,
        default=16,
        help="Tile size in pixels (default: 16)"
    )

    args = parser.parse_args()

    draw_tile_grid(args.input, args.output, args.tile_size)
