using Backend.Services;
using Backend.Models;
using Microsoft.AspNetCore.Mvc;

namespace Backend.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ResultsController : ControllerBase
{
    private readonly ResultsService _svc;
    private readonly IWebHostEnvironment _env;
    private readonly IConfiguration _cfg;

    public ResultsController(ResultsService svc, IWebHostEnvironment env, IConfiguration cfg)
    { _svc = svc; _env = env; _cfg = cfg; }

    [HttpGet]
    public IActionResult GetAll() => Ok(_svc.ListImageKeys());

    [HttpGet("{key}")]
    public IActionResult GetOne(string key)
    {
        var dto = _svc.GetByKey(key);
        return dto is null ? NotFound() : Ok(dto);
    }
}