namespace Backend.Models;

public class ImageResultDto
{
    public string Image { get; set; } = "";
    public List<DetectionDto> Local { get; set; } = new();
    public CloudResultDto Cloud { get; set; } = new();
}